from typing import Generator


def main() -> None:
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        seeds = [int(n) for n in lines.pop(0).split(":")[1].strip().split(" ")]
        lines.pop(0)  # skip line

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
                        create_generator(destination_start, source_start, range_)
                    )

                    next_line = lines.pop(0)

        lowest_location = None

        def get_mapped_value(map_name: str, key: int) -> int:
            generators = maps[map_name]
            value = key
            for generator in generators:
                result = generator(key)
                print(result)
                if result != -1:
                    value = result
                    break
            return value

        for i, seed in enumerate(seeds):
            soil_type = get_mapped_value("seed-to-soil map:", seed)
            fertilizer_type = get_mapped_value("soil-to-fertilizer map:", soil_type)
            water_type = get_mapped_value("fertilizer-to-water map:", fertilizer_type)
            light_type = get_mapped_value("water-to-light map:", water_type)
            temperature_type = get_mapped_value("light-to-temperature map:", light_type)
            humidity_type = get_mapped_value(
                "temperature-to-humidity map:", temperature_type
            )
            location = get_mapped_value("humidity-to-location map:", humidity_type)

            if lowest_location is None:
                lowest_location = location
            elif location < lowest_location:
                lowest_location = location

            print(len(seeds) - i)

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


if __name__ == "__main__":
    main()
