#include <iostream>
#include <cstdlib>
#include <vector>
#include <input.h>
#include <random>
#include <algorithm>


void shuffle_vector(std::vector<int>& v)
{
    std::random_device rd;
    std::mt19937 g{rd()};

    std::shuffle(v.begin(), v.end(), g);
}


void sort(std::vector<int>& data, std::size_t start, std::size_t end, bool shuffle=true)
{
    if (shuffle) shuffle_vector(data);

    std::size_t low{start+1};
    std::size_t high{end};

    while (low < high)
    {
        // seek left to find first entry greater than first entry
        for (; low<=high; ++low)
        {
            if (data[low] > data[start]) break;
        }
        // seek right to find first entry less than than first entry
        for (; high>start; --high)
        {
            if (data[high] < data[start]) break;
        }

        if (low < high)
        {
            std::swap(data[low], data[high]);
        }
    }

    if (data[high] < data[start])
    {
        // swap start with high (which is now the bottom index of the partition
        std::swap(data[start], data[high]);

        // sort items before the partition (high)
        if (high - start >= 2)
        {
            sort(data, start, high-1, false);
        }
        // sort items after the partition (high)
        if (end - high >= 2)
        {
            sort(data, high+1, end, false);
        }
    }
    else if (end - start >= 2)
    {
        // Now swap took place.  Start was in the correct position.
        // Sort data after start
        sort(data, start+1, end, false);
    }
}

int main()
{
    std::vector<int> v{std::move(get_data<int>())};

    sort(v, 0, v.size()-1);

    for (const auto i: v)
    {
        std::cout << i << ",";
    }
    std::cout << std::endl;

    return EXIT_SUCCESS;
}

