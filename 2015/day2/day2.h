#pragma once
#include "../Problem.h"
#include <vector>
#include <sstream>
#include <ranges>
#include <string_view>
#include <algorithm>

class Day2 : public Problem {
private:
    enum MeasureType {
        LENGTH,
        WIDTH,
        HEIGHT
    };
    vector<vector<int>> measures;
public:
    Day2() : Problem("day2") {
        solve();
    }
protected:
    void parse() {
        ifstream istream;
        istream.open(inputFile);
        string line;
        while (getline(istream, line)) {
            auto splittedStrings = ranges::split_view(line, 'x')
                | views::transform([](const auto& r) -> int { return stoi(rangeToString(r)); })
                | views::common;
            vector<int> vals(splittedStrings.begin(), splittedStrings.end());
            measures.emplace_back(std::move(vals));
        }
    }
    void part1() {
        auto areaView = measures
            | views::transform([](const vector<int>& boxMeasure) {
                auto a1 = boxMeasure[LENGTH] * boxMeasure[WIDTH];
                auto a2 = boxMeasure[WIDTH] * boxMeasure[HEIGHT];
                auto a3 = boxMeasure[HEIGHT] * boxMeasure[LENGTH];
                return vector<int>{ a1, a2, a3 };
                })
            | views::common;
        int sum = accumulate(areaView.begin(), areaView.end(), 0, [](int sum, const vector<int>& boxMeasures) {
            return sum + 2 * boxMeasures[LENGTH] + 2 * boxMeasures[HEIGHT] + 2 * boxMeasures[WIDTH] + min(boxMeasures[LENGTH], min(boxMeasures[HEIGHT], boxMeasures[WIDTH]));
            });
        cout << sum << endl;
    }
    void part2() {
        auto transformedView = measures
            | views::transform([](const vector<int>& boxMeasure) {
                auto p1 = 2 * boxMeasure[LENGTH] + 2 * boxMeasure[WIDTH];
                auto p2 = 2 * boxMeasure[WIDTH] + 2 * boxMeasure[HEIGHT];
                auto p3 = 2 * boxMeasure[HEIGHT] + 2 * boxMeasure[LENGTH];
                return pair<int, int>{ min(p1, min(p2, p3)), boxMeasure[LENGTH] * boxMeasure[HEIGHT] * boxMeasure[WIDTH]};
                })
            | views::common;
        int sum = accumulate(transformedView.begin(), transformedView.end(), 0, [](int sum, const pair<int, int>& minPerimAndArea) {
            return sum + minPerimAndArea.first + minPerimAndArea.second;
            });
        cout << sum << endl;
    }
};