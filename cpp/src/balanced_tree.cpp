#include <memory>
#include <cstdlib>

enum class Color
{
    BLACK,
    RED,
};

class Node
{
private:

    int key;
    Color color;

    Node* left{nullptr};
    Node* right{nullptr};

public:
    Node(int key, Color color=Color::BLACK): key{key}, color{color} {}

    ~Node()
    {
        delete left;
        delete right;
    }

    friend Node * rotateLeft(Node *);
    friend Node * rotateRight(Node *);
    friend void flipColors(Node *);
    friend Node * correct(Node *);

    void put(int key)
    {
        if (key < this->key)
        {
            if (!left)
            {
                left = new Node(key, Color::RED);
            }
            else
            {
                left->put(key);
            }
        }
        else if (key > this->key)
        {
            if (!right)
            {
                right = new Node(key, Color::RED);
            }
            else
            {
                right->put(key);
            }
        }

        if (right)
        {
            right = correct(right);
        }
        if (left)
        {
            left = correct(left);
        }
    }
};

Node * rotateLeft(Node * node)
{
    Node * temp = node->right;
    node->right = temp->left;
    temp->left = node;
    temp->color = node->color;
    node->color = Color::RED;
    return temp;
}

Node * rotateRight(Node * node)
{
    Node * temp = node->left;
    node->left = temp->right;
    temp->right = node;
    temp->color = node->color;
    node->color = Color::RED;
    return temp;
}

void flipColors(Node * node)
{
    node->color = Color::RED;
    node->left->color = Color::BLACK;
    node->right->color = Color::BLACK;
}

Node * correct(Node * node)
{
    if ((node->left && node->left->color == Color::BLACK) &&
        (node->right && node->right->color == Color::RED))
    {
        node = rotateLeft(node);
    }
    if (node->left && node->left->color == Color::RED &&
        node->left->left && node->left->left->color == Color::RED)
    {
        node = rotateRight(node);
    }
    if (node->left && node->left->color == Color::RED &&
        node->right && node->right->color == Color::RED)
    {
        flipColors(node);
    }
    return node;
}

int main()
{
    Node n{1};

    return EXIT_SUCCESS;
}
