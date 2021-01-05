#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <utility>

template <typename T>
std::vector<T> get_data()
{
    std::string s;
    std::stringstream stream;

    do
    {
        std::getline(std::cin, s);
        stream << s << "\n";
    } while (s != "q");

    T temp;
    std::vector<int> v;

    while (true)
    {
        stream >> temp;
        if (stream.fail()) break;
        v.push_back(temp);
    }

    return v;
}

template <typename K, typename V>
std::vector<std::pair<K, V>> get_key_values()
{
    std::string s;
    std::stringstream stream;

    do
    {
        std::getline(std::cin, s);
        stream << s << "\n";
    } while (s != "q");

    K key;
    V value;
    std::vector<std::pair<K, V>> v;

    while (true)
    {
        stream >> key >> value;
        if (stream.fail()) break;
        v.push_back(std::make_pair(key, value));
    }

    return v;
}
