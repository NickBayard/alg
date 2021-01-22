#include <unordered_set>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <stack>
#include <algorithm>

class DirectedGraph
{
private:
    std::vector<std::vector<std::size_t>> m_edges;
    std::size_t num_vertices;

public:
    DirectedGraph(std::size_t count, std::vector<std::pair<std::size_t, std::size_t>> edges):
        num_vertices{count}
    {
        m_edges.resize(count);

        for (std::pair<std::size_t, std::size_t> edge: edges)
        {
            std::vector<std::size_t>& v{m_edges[edge.first]};

            if (std::find(v.begin(), v.end(), edge.second) == v.end())
            {
                v.push_back(edge.second);
            }
        }
    }

    std::size_t size() { return num_vertices; }

    const std::vector<std::size_t>& adjacent(std::size_t source)
    {
        return m_edges[source];
    }

    DirectedGraph reverse()
    {
        std::vector<std::pair<std::size_t, std::size_t>> edges;

        for (std::size_t source{}; source<m_edges.size(); ++source)
        {
            for (std::size_t dest: m_edges[source])
            {
                edges.push_back(std::make_pair(dest, source));
            }
        }
        return DirectedGraph(num_vertices, edges);
    }
};

class StronglyConnectedComponents
{
private:
    std::vector<bool> marked;
    std::stack<std::size_t> m_stack;
    std::vector<std::vector<std::size_t>> components;
    DirectedGraph graph;
    std::size_t count{};

public:
    StronglyConnectedComponents(DirectedGraph& graph): graph{graph}
    {
        marked.resize(graph.size());
    }

    void run()
    {
        build_stack();

        for (std::size_t i{}; i<marked.size(); ++i)
        {
            marked[i] = false;
        }

        graph = graph.reverse();
        collect_components();
    }

private:
    void build_stack()
    {
        for (std::size_t vertex{}; vertex<graph.size(); ++vertex)
        {
            if (!marked[vertex])
            {
                marked[vertex] = true;
                dfs_stack(vertex);
                m_stack.push(vertex);
            }
        }
    }

    void dfs_stack(std::size_t source)
    {
        for (std::size_t adj: graph.adjacent(source))
        {
            if (!marked[adj] && (adj != source))
            {
                marked[adj] = true;
                dfs_stack(adj);
                m_stack.push(adj);
            }
        }
    }

    void collect_components()
    {
        std::size_t vertex;
        while (!m_stack.empty())
        {
            vertex = m_stack.top();
            m_stack.pop();

            if (!marked[vertex])
            {
                std::vector<std::size_t> comp;
                dfs_component(vertex, comp);
                if (comp.size())
                    components.push_back(comp);
            }
        }
    }

    void dfs_component(std::size_t source, std::vector<std::size_t>& comp)
    {
        comp.push_back(source);
        marked[source] = true;

        for (std::size_t adj: graph.adjacent(source))
        {
            if (!marked[adj] && (adj != source))
            {
                dfs_component(adj, comp);
            }
        }
    }
};
