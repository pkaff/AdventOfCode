#pragma once
#include "../Problem.h"
#include <utility>
#include <algorithm>
#include <ranges>
#include <numeric>

class Day1 : public Problem {
private:
    string input;
public:
    Day1() : Problem("day1") {
        solve();
    }
protected:
    void parse() {
        ifstream istream;
        istream.open(inputFile);
        getline(istream, input);
    }
    void part1() {
        auto res = accumulate(input.begin(), input.end(), 0, [](int sum, const char& c) {
            return sum + (c == '(' ? 1 : c == ')' ? -1 : 0);
            });
        cout << res << endl;
    }
    void part2() {
        int sum = 0;
        for (size_t ix = 0; ix < input.size(); ++ix) {
            auto c = input[ix];
            sum += (c == '(' ? 1 : c == ')' ? -1 : 0);
            if (sum == -1) {
                cout << (ix + 1) << endl;
                break;
            }
        }
    }
};