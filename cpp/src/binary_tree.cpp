#include <iostream>
#include <algorithm>
#include <vector>
#include <input.h>
#include <memory>

template <typename K>
class Node
{
private:
    K key;
    std::unique_ptr<Node> left{nullptr};
    std::unique_ptr<Node> right{nullptr};
public:
    Node(K key): key{key} {}
};

template <typename K>
class BST
{
private:
    std::unique_ptr<Node<K>> root{nullptr};

public:
    BST() = default;

    V& get(K key)
    {
        assert(root != nullptr);
        return root.get(key);
    }

    void del(K key)
    {
        assert(root != nullptr);
        if (!root.del(key))
        {
            clean();
        }
    }

    void put(K key, V value)
    {
        if (!root)
        {
            root = std::make_unique<Node<K, V>>(key, value);
        }
        else
        {
            root.put(key, value);
        }
    }
};


int main()
{
    std::vector<int> v{std::move(get_vector<int>())};

    BST bst;

    for auto

    std::cout << std::endl;

    return EXIT_SUCCESS;
}
