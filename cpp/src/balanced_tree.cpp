#include <memory>
#include <cstdlib>

class Node
{
private:
    enum class Color
    {
        BLACK,
        RED,
    };

    int key;
    Color color;

    Node* left{nullptr};
    Node* right{nullptr};

    Node* rotateLeft()
    {
        Node* temp = right;
        right = temp->left;
        temp->left = this;
        temp->color = color;
        color = Color::RED;
        return temp;
    }

    Node* rotateRight()
    {
        return this;
    }

    void flipColors()
    {
    }

public:
    Node(int key, Color color=Color::BLACK): key{key}, color{color} {}

    ~Node()
    {
        delete left;
        delete right;
    }

    void put(int key)
    {
    }
};

int main()
{
    Node n{1};

    return EXIT_SUCCESS;
}
