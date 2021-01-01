#include <cstdlib>
#include <iostream>
#include <memory>

template <class T>
class Stack
{
private:
    static constexpr std::size_t min_capacity{10};
    std::unique_ptr<T[]> backing{nullptr};
    std::size_t top{};
    std::size_t capacity;

    void copy_new()
    {
        std::unique_ptr<T[]> new_back{std::make_unique<T[]>(capacity)};

        for (std::size_t i{}; i < top; ++i)
        {
            new_back[i] = this->backing[i];
        }
        this->backing = std::move(new_back);
    }

    void grow()
    {
        capacity *= 2;
        copy_new();
    }

    void shrink()
    {
        capacity /= 2;
        copy_new();
    }

public:
    Stack(const std::size_t size=min_capacity): capacity{size}, backing{std::make_unique<T[]>(size)} {}

    friend std::ostream& operator<<(std::ostream& out, const Stack<T>& s)
    {
        out << "Stack<" << s.capacity << ">(";

        for (std::size_t i{}; i < s.top; ++i)
        {
            out << s.backing[i];
            if ((s.top) && (i != (s.top - 1)))
            {
                out << ",";
            }
        }

        out << ")";

        return out;
    }

    void push(const T& value)
    {
        backing[top] = value;
        ++top;

        if (top >= capacity)
        {
            grow();
        }
    }

    T pop()
    {
        if (!top)
        {
            throw "Stack is empty";
        }

        T temp = backing[top-1];
        --top;

        if ((top < (capacity / 2)) && (capacity > min_capacity))
        {
            shrink();
        }

        return temp;
    }
};


int main()
{
    Stack<int> stack;

    for (int i{}; i < 25; ++i)
    {
        stack.push(i);
    }

    std::cout << stack << std::endl;

    for (int i{}; i < 20; ++i)
    {
        try
        {
            std::cout << "Popped: " << stack.pop() << "\n";
        }
        catch (const char * s)
        {
            std::cout << "Exception caught: " << s << std::endl;
            return EXIT_FAILURE;
        }
    }

    std::cout << stack << std::endl;

    return EXIT_SUCCESS;
}
