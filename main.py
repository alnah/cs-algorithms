import math

"""
Remember:
- Log(16, base 2) means "How many times 2 need to be multiplied by itself to react 16?"

From slow to fast:
- logarithmic: log(n, b)
- linear: (a * n) + b
- quadratic: n ** n
- factorial: !n

Excellent:
- hashmap lookup: O(1)
Great:
- binary search in sorted array: 0(log(n))
Fair:
- iteration: O(n)
- sequence of iterations: 0(nm)
Horrible:
- nested iterations: 0(n^2)
- recursive branching: 0(2^n)
Hell:
- generating all permutations: O(n!)
"""


def main():
    print(get_avg_brand_followers([
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
], "cosmo"))

def find_minimum(nums: list[int]) -> int | None:
    minimum = float("inf")
    if not nums:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return int(minimum)


def sum(nums: list[int]) -> int:
    total = 0
    if not nums:
        return total
    for num in nums:
        total += num
    return total


def average_followers(nums: list[int]) -> int | None:
    if not nums:
        return None
    total = 0
    for num in nums:
        total += num
    return round(total / len(nums))


def median_followers(nums: list[int]) -> float | None:
    if not nums:
        return None
    nums_sorted = sorted(nums)
    length = len(nums_sorted)
    mid = length // 2
    if length % 2 == 1:
        return nums_sorted[mid]
    else:
        return (nums_sorted[mid - 1] + nums_sorted[mid]) / 2


def get_estimated_spread(audiences_followers: list[int]) -> float:
    if not audiences_followers:
        return 0
    total_audience_followers = 0
    for af in audiences_followers:
        total_audience_followers += af
    average_audience_followers = total_audience_followers / len(audiences_followers)
    estimated_spread = average_audience_followers * (len(audiences_followers) ** 1.2)
    return estimated_spread


INFLUENCER_TYPE_TO_RATIO_MAP: dict[str, int] = {
    "fitness": 4,
    "cosmetic": 3,
    "other": 2,
}


def get_follower_prediction(
    follower_count: int,
    influencer_type: str,
    num_months: int,
) -> int:
    prediction = 0
    if not follower_count or not num_months:
        return prediction
    if not influencer_type:
        raise ValueError("Influencer type must be a non-empty string")
    ratio = 0
    if influencer_type not in ["fitness", "cosmetic"]:
        ratio = INFLUENCER_TYPE_TO_RATIO_MAP["other"]
    else:
        ratio = INFLUENCER_TYPE_TO_RATIO_MAP[influencer_type]
    prediction = follower_count * (ratio**num_months)
    return prediction


def get_influencer_score(
    num_followers: int,
    average_engagement_percentage: float,
) -> float:
    return average_engagement_percentage * math.log(num_followers, 2)


def num_possible_orders(num_posts: int) -> int:
    if num_posts == 0:
        return 0
    possible_orders = 1
    for n in range(num_posts, 1, -1):
        possible_orders *= n
    return possible_orders


def decayed_followers(
    intl_followers: int, fraction_lost_daily: float, days: int
) -> float:
    if intl_followers == 0 or days == 0:
        return 0
    remaining = intl_followers
    if fraction_lost_daily == 0:
        return remaining
    for _ in range(days):
        print(remaining)
        remaining -= remaining * fraction_lost_daily
        print(remaining)
    return remaining


def log_scale(data: list[int], base: int) -> list[float]:
    if not data:
        return []
    if base == 0 or base == 1:
        raise ValueError("Logarithm base must be 2 at least")
    return list(map(lambda d: math.log(d, base), data))


def find_max(nums: list[int]) -> float:
    maximum = float("-inf")
    if not nums:
        return maximum
    for n in nums:
        if maximum < n:
            maximum = n
    return maximum


def does_name_exist(
    first_names: list[str],
    last_names: list[str],
    full_name: str,
) -> bool:
    full_names = set(f"{f} {l}" for f, l in zip(first_names, last_names))
    return full_name in full_names

def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:
    if not brand_name:
        raise ValueError("Brand name can't by empty")
    count = 0
    if not all_handles:
        return count
    for handle in all_handles:
        for influencer in handle:
            if brand_name in influencer:
                count += 1
    return count / len(all_handles)
       
def find_last_name(names_dict, first_name) -> str | None:
    if not names_dict or not first_name:
        return None
    return names_dict.get(first_name, None)

def binary_search(target: int, array: list[int]) -> bool:
    start, end = 0, len(array) -1
    while start <= end:
        median = (start + end) // 2
        if array[median] == target:
            return True
        elif array[median] > target:
            end = median - 1
        elif array[median] < target:
            start = median + 1
    return False

def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    names = []
    for l in list_of_lists:
        names.extend(l)
    count = 0
    for n in names:
        if n == target_name:
            count += 1
    return count

def remove_duplicates(nums: list[int]) -> list[int]:
    deduped_map, deduped_list = {}, []
    for n in nums:
        deduped_map[n] = None
    for n in deduped_map:
        deduped_list.append(n)
    return deduped_list

if __name__ == "__main__":
    main()
