#pragma once
#include <string>
#include <iostream>
#include <fstream>
#include "AoCUtility.h"

using namespace std; //This is a toy project. Obviously don't do this normally...
using namespace aoc_utility; //same here

class Problem {
public:
    Problem() = delete;
    Problem(std::string&& prefix) : inputFile(std::move(prefix) + "/input.txt") {}
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