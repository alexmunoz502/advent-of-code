from typing import Generator
import itertools


def main() -> None:
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        seeds_line = [int(n) for n in lines.pop(0).split(":")[1].strip().split(" ")]
        lines.pop(0)  # skip line

        seed_ranges = []
        while len(seeds_line) > 0:
            range_start = seeds_line.pop(0)
            range_length = seeds_line.pop(0)
            range_ = (range_start, range_start + range_length)
            seed_ranges.append(range_)

        def seed_in_range(seed: int) -> bool:
            for range_ in seed_ranges:
                start, end = range_
                if start <= seed < end:
                    return True
            return False

        maps = {}

        # Create Maps
        while len(lines) > 0:
            line = lines.pop(0)
            if "map" in line:
                map_name = line
                maps[map_name] = []
                next_line = lines.pop(0)
                while len(lines) > 0 and next_line != "":
                    numbers = [int(n) for n in next_line.split(" ")]

                    destination_start = numbers[0]
                    source_start = numbers[1]
                    range_ = numbers[2]

                    maps[map_name].append(
                        create_reverse_generator(
                            destination_start, source_start, range_
                        )
                    )

                    next_line = lines.pop(0)

        lowest_location = None

        def get_mapped_value(map_name: str, key: int) -> int:
            generators = maps[map_name]
            value = key
            for generator in generators:
                result = generator(key)
                if result != -1:
                    value = result
                    break
            return value

        for i in itertools.count():
            location = i
            humidity_type = get_mapped_value("humidity-to-location map:", location)
            temperature_type = get_mapped_value(
                "temperature-to-humidity map:", humidity_type
            )
            light_type = get_mapped_value("light-to-temperature map:", temperature_type)
            water_type = get_mapped_value("water-to-light map:", light_type)
            fertilizer_type = get_mapped_value("fertilizer-to-water map:", water_type)
            soil_type = get_mapped_value("soil-to-fertilizer map:", fertilizer_type)
            seed = get_mapped_value("seed-to-soil map:", soil_type)

            if seed_in_range(seed):
                print(location)
                return

            if i % 100_000 == 0:
                # For keeping track of progress since this takes so long to run.
                print(f"{i}")

        print(lowest_location)


def create_generator(
    destination_start: int, source_start: int, range_: int
) -> Generator:
    def generator(key: int) -> int:
        if source_start <= key and key < source_start + range_:
            return key + (destination_start - source_start)
        else:
            return -1

    return generator


def create_reverse_generator(
    destination_start: int, source_start: int, range_: int
) -> Generator:
    def generator(key: int) -> int:
        if destination_start <= key and key < destination_start + range_:
            return key - (destination_start - source_start)
        else:
            return -1

    return generator


if __name__ == "__main__":
    # Note: this is a brute-force solution and so it takes like 5-8 mins to run.
    main()
