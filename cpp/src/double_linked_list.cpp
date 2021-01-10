#include <iostream>
#include <cstdlib>
#include <memory>

class List;

class Node
{
private:
    std::shared_ptr<Node> next, previous;
    int value;

public:
    Node(int value): value{value} {}

    friend class List;
    friend std::ostream& operator<<(std::ostream& out, const List& l);
};

class List
{
    using NodeT = std::shared_ptr<Node>;
private:
    NodeT head, tail;
    std::size_t size;

public:
    List(): head{nullptr}, tail{nullptr}, size{} {}

    friend std::ostream& operator<<(std::ostream& out, const List& l)
    {
        NodeT ptr{l.head};

        while (ptr)
        {
            out << ptr->value << "->";
            ptr = ptr->next;
        }
        out << "nullptr";
        return out;
    }

    std::size_t append(const int value)
    {
        NodeT node{new Node{value}};
        ++size;

        if (!head)
        {
            head = node;
            tail = node;
        }
        else
        {
            tail->next = node;
            node->previous = tail;
            tail = node;
        }
        return size;
    }

    void dedupe()
    {
        NodeT ptr{head};

        while (ptr)
        {
            if (ptr->next && ptr->next->value == ptr->value)
            {
                ptr->next = ptr->next->next;
                // shared_ptr will run out of references and delete that node
            }
            else
            {
                ptr = ptr->next;
            }
        }
    }

    void reverse()
    {
        NodeT ptr{head};
        NodeT next{nullptr};
        NodeT prev{nullptr};

        while (ptr)
        {
            head = ptr;
            next = ptr->next;
            ptr->next = prev;
            ptr->previous = next;
            prev = ptr;
            ptr = next;
        }
    }

    void printMiddleOut()
    {
        NodeT middle{head};

        // Point middle at middle node
        for (std::size_t i{}; i<size/2; ++i)
        {
            if (!middle->next)
            {
                return;
            }
            middle = middle->next;
        }
        std::cout << middle->value << " ";

        NodeT left{middle->previous};
        NodeT right{middle->next};

        while (left || right)
        {
            if (left)
            {
                std::cout << left->value << " ";
                left = left->previous;
            }
            if (right)
            {
                std::cout << right->value << " ";
                right = right->next;
            }
        }
    }

    void swap(NodeT a, NodeT b)
    {
        NodeT temp{b->next};
        b->next = a->next;
        if (b->next)
        {
            b->next->previous = b;
        }
        a->next = temp;
        if (a->next)
        {
            a->next->previous = a;
        }

        temp = b->previous;
        b->previous = a->previous;
        if (b->previous)
        {
            b->previous->next = b;
        }
        a->previous = temp;
        if (a->previous)
        {
            a->previous->next = a;
        }
    }

    std::size_t count(NodeT low, NodeT high)
    {
        NodeT it{low};

        std::size_t count{};

        while (low != high)
        {
            ++count;
            low = low->next;
        }

        return count;
    }

    void sort(NodeT start, NodeT end)
    {
        NodeT low{start};
        NodeT high{end};

        while (low != high and high->next != low)
        {
            for (;low != high; low=low->next)
            {
                if (low->value > start->value) break;
            }
            for (;high != low; high=high->previous)
            {
                if (high->value < start->value) break;
            }

            if (low != high and high->next != low)
            {
                swap(low, high);
                NodeT temp{low};
                low = high;
                high = temp;
            }
        }

        if (high->value < start->value)
        {
            swap(start, high);
            NodeT temp{start};
            start = high;
            high = temp;

            if (count(start, high) >= 2)
            {
                sort(start, high->previous);
            }
            if (count(high, end) >= 2)
            {
                sort(high->next, end);
            }
        }
        else if (count(start, end) >= 2)
        {
            sort(start->next, end);
        }
    }

    void sort()
    {
        // TODO randomize list
        sort(head, tail);
    }

};



int main()
{
    List l;
    for (int i{10}; i; --i)
    {
        l.append(i);
    }

    std::cout << l << "\n";
    l.sort();
    std::cout << std::endl;

    return EXIT_SUCCESS;
}
