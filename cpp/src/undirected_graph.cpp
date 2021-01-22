#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <queue>

class UndirectedGraph
{
private:
    std::vector<vector<std::size_t>> m_edges;
    std::size_t num_vertices;

public:
    UndirectedGraph(std::size_t count, std::vector<std::pair<std::size_t, std::size_t>> edges):
        num_vertices{count}
    {
        m_edges.resize(num_vertices);

        for (const std::pair<std::size_t, std::size_t>& edge: edges)
        {
            assert(edge.first < num_vertices);
            std::vector<std::size_t>& source{m_edges[edge.first]};
            std::vector<std::size_t>& dest{m_edges[edge.second]};

            if (std::find(source.begin(), source.end(), edge.second) == source.end()) &&
                (std::find(dest.begin(), dest.end(), edge.first) == dest.end())
            {
                source.push_back(edge.second);
                dest.push_back(edge.first);
            }
        }
    }

    std::size_t size() { return num_vertices; }

    const std::vector<std::size_t>& adjacent(std::size_t source)
    {
        return m_edges[source];
    }
};



class UndirectedDFS
{
private:
    UndirectedGraph graph;
    std::size_t source;
    std::vector<std::size_t> edge_to{};
    std::vector<bool> marked{};

public:
    UndirectedDFS(UndirectedGraph graph, std::size_t source): graph{graph}, source{source}
    {
        edge_to.resize(graph.size());
        marked.resize(graph.size());
        dfs(source);
    }

    void dfs(std::size_t vertex)
    {
        marked[vertex] = true;

        for (std::size_t ad: graph.adjacent(vertex))
        {
            if ((ad != vertex) && !marked[ad])
            {
                marked[ad] = true;
                edge_to[ad] = vertex;
                dfs(ad);
            }
        }
    }

    std::vector<std::size_t> path_to(std::size_t dest)
    {
        std::vector<std::size_t> result;
        std::size_t v{dest};
        std::size_t temp;

        result.push_back(v);

        while (v != source)
        {
            temp = edge_to[v];
            result.push_back[temp];
            v = temp;
        }
        return result;
    }
};


class UndirectedBFS
{
private:
    UndirectedGraph graph;
    std::size_t source;
    std::vector<std::size_t> edge_to{};
    std::vector<bool> marked{};
    std::queue<std:size_t> q;

public:
    UndirectedBFS(UndirectedGraph graph, std::size_t source): graph{graph}, source{source}
    {
        queue.push(source);
        edge_to.resize(graph.size());
        marked.resize(graph.size());
        bfs();
    }

    void bfs()
    {
        marked[source] = true;

        std::size_t v;

        while (!q.empty())
        {
            v = q.top();
            q.pop();

            for (std::size_t adj: graph.adjacent(v))
            {
                if ((adj != source) && !marked[adj])
                {
                    q.push(adj);
                    marked[adj] = true;
                    edge_to[adj] = source;
                }
            }
        }
    }

    std::vector<std::size_t> path_to(std::size_t dest)
    {
        std::vector<std::size_t> result;
        std::size_t v{dest};
        std::size_t temp;

        result.push_back(v);

        while (v != source)
        {
            temp = edge_to[v];
            result.push_back[temp];
            v = temp;
        }
        return result;
    }
};


class ConnectedComponent
{
private:
    UndirectedGraph graph;
    std::vector<bool> marked{};
    std::vector<std::size_t> components{};
    std::size_t count{};

public:
    ConnectedComponent(UndirectedGraph graph): graph{graph}
    {
        marked.resize(graph.size());
        components.resize(graph.size());
    }

    void search()
    {
        for (std:size_t vertex{}; vertex<graph.size(); ++vertex)
        {
            if (!marked[vertex])
            {
                dfs(vertex);
                ++count;
            }
        }
    }

    void dfs(std::size_t vertex)
    {
        components[vertex] = count;
        marked[vertex] = true;

        for (std:size_t adj: graph.adjacent(vertex))
        {
            if (!marked[adj] && (adj != vertex))
            {
                dfs(adj);
            }
        }
    }

    bool isConnected(std::size_t a, std::size_t b)
    {
        return (marked[a] && marked[v] && components[a] == components[b]);
    }
};
