def compute_max_chain(words):
    words_set = set(words)
    dp = {}

    words = length_bucket_sort(words)

    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i + 1:]
            if prev in words_set:
                dp[word] = max(dp[word], dp.get(prev, 1) + 1)

    return max(dp.values()) if dp else 1


def length_bucket_sort(words):
    if not words:
        return words

    max_len = max(len(word) for word in words)
    buckets = [[] for _ in range(max_len + 1)]

    for word in words:
        buckets[len(word)].append(word)

    sorted_words = []
    for bucket in buckets:
        sorted_words.extend(bucket)

    return sorted_words


def main():
    with open("src/wchain.in", "r", encoding="utf-8") as f:
        n = int(f.readline())
        words = [f.readline().strip() for _ in range(n)]

    result = compute_max_chain(words)

    with open("src/wchain.out", "w", encoding="utf-8") as f:
        f.write(str(result) + "\n")


if __name__ == "__main__":
    main()
