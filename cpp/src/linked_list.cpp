#include <iostream>
#include <cstdlib>
#include <memory>

template <class T>
class Node
{
private:
    T _value;
    Node * _next{nullptr};

public:
    Node(T value): _value{value} {}

    Node * insert_after(const T& value)
    {
        auto temp = _next;
        _next = new Node{value};
        _next->_next = temp;
        return _next;
    }

    friend std::ostream& operator<<(std::ostream& out, const Node* n)
    {
        out << "Node<" << n->_value << ">";

        auto node = n->_next;
        while (node)
        {
            out << "->Node<" << node->_value << ">";
            node = node->_next;
        }
        return out;
    }

    ~Node() {
        std::cout << "Destroying " << _value << "\n";
        delete _next;
    }

};


int main()
{
    constexpr int start{10};
    auto node = std::make_unique<Node<int>>(start);
    auto ptr{node.get()};
    for (int i{start-1}; i >= 0; --i)
    {
        ptr = ptr->insert_after(i);
    }
    std::cout << node.get() << std::endl;

    return EXIT_SUCCESS;
}
