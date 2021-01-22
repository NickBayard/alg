#include <iostream>
#include <cstdlib>
#include <cstdint>
#include <string>
#include <utility>
#include <memory>
#include <cassert>
#include <stdexcept>


static constexpr std::size_t SMALL_PRIME{31};


std::size_t get_hash(const std::uint64_t i, const std::size_t m)
{
    return i % m;
}

std::size_t get_hash(double d, const std::size_t m)
{
    std::uint64_t * p{reinterpret_cast<std::uint64_t*>(&d)};
    return *p % m;
}

std::size_t get_hash(const std::string& s, const std::size_t m)
{
    std::size_t h{0};

    for (const std::size_t i : s)
    {
        h = (SMALL_PRIME * h + i) % m;
    }
    return h;
}

class Hash
{
    using Entry = std::unique_ptr<std::pair<std::uint64_t, std::string>>;

private:
    static constexpr std::size_t sizes[]{131, 257, 521, 1031, 2053};
    std::size_t size_index{};
    std::size_t size;
    Entry * backing;

public:
    Hash(): size{sizes[size_index]}, backing{new Entry[size]} {}

    void grow()
    {
        ++size_index;
        std::size_t old_size{size};
        size = sizes[size_index];

        Entry * new_backing{new Entry[size]};

        for (std::size_t i{}; i < old_size; ++i)
        {
            if (backing[i])
            {
                std::size_t h = get_hash(backing[i]->first, size);
                new_backing[h] = std::move(backing[i]);
            }
        }
        backing = new_backing;
    }

    void put(std::uint64_t key, std::string value)
    {
        std::size_t h = get_hash(key, size);

        assert (h < size);

        if (!backing[h])
        {
            backing[h] = std::make_unique<std::pair<std::uint64_t, std::string>>(std::make_pair(key, value));
        }
        else if (backing[h]->first == key)
        {
            // same key
            backing[h]->second = value;
        }
        else
        {
            // hash collision
            grow();
            put(key, value);
        }
    }

    std::string& get(std::uint64_t key)
    {
        std::size_t h = get_hash(key, size);

        assert (h < size);

        if (!backing[h])
        {
            throw std::runtime_error("Miss!");
        }
        else
        {
            return backing[h]->second;
        }
    }

    friend std::ostream& operator<<(std::ostream& out, const Hash& h)
    {
        out << "Hash:\n";
        for (std::size_t i{}; i<h.size; ++i)
        {
            if (h.backing[i])
            {
                out << i << ": " << h.backing[i]->first << ", " << h.backing[i]->second << "\n";
            }
            else
            {
                out << i << ": nullptr\n";
            }
        }
        return out;
    }
};

int main()
{
    Hash h;

    h.put(1025, "hello");
    h.put(1026, "world");

    std::cout << h << "\n";

    return EXIT_SUCCESS;
}
