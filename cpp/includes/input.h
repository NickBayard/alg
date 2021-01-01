#include <iostream>
#include <string>
#include <vector>
#include <sstream>

template <typename T>
std::vector<T> get_vector()
{
    std::string s;
    std::stringstream stream;

    do
    {
        std::getline(std::cin, s);
        stream << s << "\n";
    } while (s != "q");

    int temp;
    std::vector<int> v;

    while (true)
    {
        stream >> temp;
        if (stream.fail()) break;
        v.push_back(temp);
    }

    return v;
}
