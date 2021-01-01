#include <iostream>
#include <cstdlib>
#include <memory>

template <class T>
class Array
{
private:
    std::size_t capacity;
    std::size_t length{};
    std::unique_ptr<T[]> backing;

    void grow()
    {
        capacity *= 2;
        std::unique_ptr<T[]> backing{std::make_unique<T[]>(capacity)};

        for (std::size_t i{}; i <= length; ++i)
        {
            backing[i] = this->backing[i];
        }
        this->backing = std::move(backing);
    }

public:
    Array(std::size_t capacity=10):
        capacity{capacity},
        backing{std::make_unique<T[]>(capacity)} {}

    void insert(const T& value)
    {
        backing[length] = value;
        ++length;

        if (length >= capacity)
        {
            grow();
        }
    }

    const T& operator[](const std::size_t index) const
    {
        return backing[index];
    }

    const std::size_t getLength() const {return length;}
    const std::size_t getCapacity() const {return capacity;}

    friend std::ostream& operator<<(std::ostream& out, const Array<T>& a)
    {
        out << "Array<";

        for (std::size_t i{}; i < a.length; ++i)
        {
            out << a[i] << " ";
        }
        out << ">";

        return out;
    }
};


int main()
{
    Array<int> a{10};

    for (int i{}; i < 30; ++i)
    {
        a.insert(i);
    }

    std::cout << a << "\ncapacity: " << a.getCapacity() << std::endl;;

    return EXIT_SUCCESS;
}
