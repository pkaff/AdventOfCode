#pragma once
#include <string>
#include <iostream>
#include <fstream>

using namespace std; //This is a toy project. Obviously don't do this normally...

class Problem {
public:
    Problem() = delete;
    Problem(std::string&& inputFile) : inputFile(std::move(inputFile)) {}
protected:
    std::string inputFile;

    void solve() {
        parse();
        part1();
        part2();
    }
    virtual void parse() = 0;
    virtual void part1() = 0;
    virtual void part2() = 0;
};