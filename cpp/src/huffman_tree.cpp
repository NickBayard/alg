#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <unordered_map>

struct Tree
{
    char character;
    unsigned int count;
    Tree * left{nullptr};
    Tree * right{nullptr};

    Tree(char c, unsigned int count): character{c}, count{count} {}
};

class MinHeap
{
private:
    std::vector<Tree*> data;
    std::size_t bottom{};

    void swim()
    {
        std::size_t index{bottom};
        std::size_t parent;

        while (index > 1)
        {
            parent = index / 2;

            if (data[index]->count >= data[parent]->count)
                break;

            std::swap(data[index], data[parent]);
            index = parent;
        }
    }

    void sink()
    {
        std::size_t index{1};
        std::size_t child{index * 2};

        while (child <= bottom)
        {
            if ((child < bottom) and (data[child+1]->count > data[child]->count))
                child += 1;

            if (data[index]->count <= data[child]->count)
                break;

            std::swap(data[index], data[child]);
            index = child;
            child *= 2;
        }
    }

public:
    MinHeap(const std::string& s)
    {
        std::unordered_map<char, unsigned int> freq;

        for (char c: s)
        {
            if (freq.find(c) == freq.end())
            {
                freq[c] = 1;
            }
            else
            {
                freq[c] = freq[c] + 1;
            }
        }

        data.push_back(nullptr);

        for (std::unordered_map<char, unsigned int>::iterator it{freq.begin()}; it != freq.end(); ++it)
        {
            push(new Tree{it->first, it->second});
        }
    }

    void push(Tree* node)
    {
        data.push_back(node);
        ++bottom;
        swim();
    }

    Tree* pop()
    {
        if (!bottom)
            throw std::range_error("oops");

        Tree* temp = data[1];
        data[1] = data[bottom];
        data[bottom] = nullptr;
        --bottom;

        sink();

        return temp;
    }

    bool size() { return bottom; }
};

Tree * buildTree(MinHeap& heap)
{
    Tree* root{nullptr};

    while (heap.size() > 1)
    {
        Tree* a{heap.pop()};
        Tree* b{heap.pop()};

        unsigned int parent{a->count + b->count};

        root = new Tree{0, parent};

        if (a->count > b->count)
        {
            root->right = a;
            root->left = b;
        }
        else
        {
            root->left = a;
            root->right = b;
        }

        heap.push(root);
    }

    if (heap.size() == 1)
    {
        root = heap.pop();
    }

    return root;
}

int main()
{
    std::string s{"sadfasgagdsfgsdafsdafdasfsdfadsfsadasdfasdfasdssfdaasdffas"};
    MinHeap heap{s};
    Tree* root{buildTree(heap)};

    return EXIT_SUCCESS;
}
