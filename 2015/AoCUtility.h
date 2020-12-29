#pragma once
#include <ranges>
#include <utility>
#include <string>
#include <concepts>
#include <vector>

namespace aoc_utility {

// how to require that the view T's underlying data is convertible to char?
/*template<typename T>
concept StringData = requires(T t) {
    { t.data() } -> std::convertible_to<char>;
};*/
template<typename R>
concept StringRange = std::ranges::range<R>; //&& StringData<R>;

template<StringRange R>
std::string rangeToString(R&& rng) {
    auto v = std::views::common(std::forward<R>(rng));
    return std::string(v.begin(), v.end());
}

inline constexpr auto trim_front = std::views::drop_while(::isspace);
inline constexpr auto trim_back =
                std::views::reverse
                | std::views::drop_while(::isspace)
                | std::views::reverse;
inline constexpr auto trim = trim_front | trim_back;

std::string trimStr(const std::string& str) {
    return rangeToString(str | trim);
}

} //namespace aoc_utility