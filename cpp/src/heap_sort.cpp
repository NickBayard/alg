#include <iostream>
#include <algorithm>
#include <vector>
#include <stdexcept>
#include <input.h>


template <class T>
class Heap
{
private:
    std::size_t bottom{};
    std::vector<T> backing;

    void swim()
    {
        std::size_t index{bottom};
        std::size_t parent;

        while (index > 1)
        {
            parent = index / 2;
            if (backing[parent] >= backing[index])
            {
                break;
            }
            std::swap(backing[parent], backing[index]);
            index = parent;
        }
    }

    void sink()
    {
        std::size_t index{1};
        std::size_t child;

        while (index * 2 <= bottom)
        {
            child = index * 2;

            if ((child < bottom) && (backing[child] < backing[child+1]))
            {
                child += 1;
            }

            if (backing[child] <= backing[index])
            {
                break;
            }

            std::swap(backing[child], backing[index]);
            index = child;
        }

    }

public:
    Heap()
    {
        //T temp{};
        backing.push_back(T{});
    }

    void push(const T& value)
    {
        backing.push_back(value);
        ++bottom;
        swim();
    }

    T pop()
    {
        if(!bottom)
        {
            throw std::range_error("Heap empty!");
        }

        T temp = backing[1];
        backing[1] = T{};
        std::swap(backing[1], backing[bottom]);
        --bottom;

        sink();

        return temp;
    }

    bool empty() { return (!bottom); }
};


int main()
{
    std::vector<int> v{std::move(get_vector<int>())};
    Heap<int> heap;

    for (auto i: v)
    {
        heap.push(i);
    }

    while (!heap.empty())
    {
        std::cout << heap.pop() << ",";
    }
    std::cout << std::endl;

    return EXIT_SUCCESS;
}
