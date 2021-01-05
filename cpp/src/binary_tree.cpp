#include <iostream>
#include <algorithm>
#include <vector>
#include <input.h>
#include <memory>
#include <utility>
#include <string>
#include <exception>

template <typename K, typename V>
class Node
{
private:
    K key;
    V value;
    std::size_t size;
    std::unique_ptr<Node> left{nullptr};
    std::unique_ptr<Node> right{nullptr};

    void recalc_size()
    {
        size = (left ? left->size : 0) + (right ? right->size : 0) + 1;
    }
public:
    Node(K key, V value, std::size_t size): key{key}, value{value}, size{size} {}

    V& get(K key)
    {
        if (key == this->key)
        {
            return value;
        }
        else if ((key < this->key) && left)
        {
            return left->get(key);
        }
        else if ((key > this->key) && right)
        {
            return right->get(key);
        }

        throw std::runtime_error("Key not found");
    }

    void put(K key, V value)
    {
        if (key < this->key)
        {
            if (!left)
            {
                left = std::make_unique<Node>(key, value, 1);
            }
            else
            {
                left->put(key, value);
            }
        }
        else if (key > this->key)
        {
            if (!right)
            {
                right = std::make_unique<Node>(key, value, 1);
            }
            else
            {
                right->put(key, value);
            }
        }
        recalc_size();
    }

    Node * min()
    {
        if (left)
        {
            return left->min();
        }
        else
        {
            return this;
        }
    }

    Node * max()
    {
        if (right)
        {
            return right->max();
        }
        else
        {
            return this;
        }
    }

    bool del(K key)
    {
        if (key == this-> key)
        {
            if (left)
            {
                // Find max node in left
                Node * _max = left->max();
                key = _max->key;
                value = _max->value;

                if (!left->del(_max->key))
                {
                    left = nullptr;
                }
                recalc_size();
                return true;
            }
            else if (right)
            {
                // Find min node in right
                Node * _min = right->min();
                key = _min->key;
                value = _min->value;

                if(!right->del(_min->key))
                {
                    right = nullptr;
                }
                recalc_size();
                return true;
            }
            else
            {
                // Delete me!
                return false;
            }
        }
        else if((key < this->key) && left)
        {
            if (!left->del(key))
            {
                left = nullptr;
            }
            recalc_size();
            return true;
        }
        else if((key > this->key) && right)
        {
            if (!right->del(key))
            {
                right = nullptr;
            }
            recalc_size();
            return true;
        }

        throw std::runtime_error("Key not found");
    }

    Node * select(std::size_t rank)
    {
        std::size_t lsize = (left ? left->size : 0);

        if (rank == lsize)
        {
            return this;
        }
        else if (left && (rank < lsize))
        {
            return left->select(rank);
        }
        else if (right && (rank > lsize))
        {
            return right->select(rank - lsize - 1);
        }

        throw std::runtime_error("Invalid rank");
    }

    std::size_t rank(K key)
    {
        std::size_t lsize = (left ? left->size : 0);

        if (key == this->key)
        {
            return lsize;
        }
        else if (left && (key < this->key))
        {
            return left->rank(key);
        }
        else if(right && (key > this->key))
        {
            return right->rank(key) + lsize + 1;
        }

        throw std::runtime_error("Invalid key");
    }

};

template <typename K, typename V>
class BST
{
private:
    std::unique_ptr<Node<K, V>> root{nullptr};

public:
    BST() = default;

    V& get(K key)
    {
        if(!root)
        {
            throw std::runtime_error("Key not found");
        }
        return root->get(key);
    }

    void del(K key)
    {
        if(!root)
        {
            throw std::runtime_error("Key not found");
        }
        if (!root->del(key))
        {
            root = nullptr;
        }
    }

    void put(K key, V value)
    {
        if (!root)
        {
            root = std::make_unique<Node<K, V>>(key, value, 1);
        }
        else
        {
            root->put(key, value);
        }
    }
};


int main()
{
    std::vector<std::pair<int, std::string>> v{std::move(get_key_values<int, std::string>())};

    BST<int, std::string> bst;

    for (auto p: v)
    {
        bst.put(p.first, p.second);
    }


    std::string temp;
    for (auto p: v)
    {
        temp = bst.get(p.first);
        std::cout << p.first << ": " << p.second << "->" << temp << "\n";

        bst.del(p.first);

        try
        {
            temp = bst.get(p.first);
            std::cout << p.first << " not successfully deleted!\n";
        }
        catch (const std::runtime_error& ex)
        {
            std::cout << p.first << " successfully deleted\n";
        }
    }

    return EXIT_SUCCESS;
}
