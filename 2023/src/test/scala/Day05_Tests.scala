import main.scala.day05._
import main.scala.day13.parseFile

class Day5_Tests extends munit.FunSuite {
  test("Test Parsing") {
    val lines = List(
      "seeds: 79 14 55 13",
      "",
      "seed-to-soil map:",
      "50 98 2",
      "52 50 48",
      "",
      "soil-to-fertilizer map:",
      "0 15 37",
      "37 52 2",
      "39 0 15",
      "",
      "fertilizer-to-water map:",
      "49 53 8",
      "0 11 42",
      "42 0 7",
      "57 7 4",
      "",
      "water-to-light map:",
      "88 18 7",
      "18 25 70",
      "",
      "light-to-temperature map:",
      "45 77 23",
      "81 45 19",
      "68 64 13",
      "",
      "temperature-to-humidity map:",
      "0 69 1",
      "1 0 69",
      "",
      "humidity-to-location map:",
      "60 56 37",
      "56 93 4"
    )
    val obtained = parseAlmanac(lines)
    val expected = new Almanac(
        seeds = List(79,14,55,13), 
        seedsToSoil = List(List(50, 98, 2),List(52,50,48)), 
        soilToFertilizer = List(List(0, 15, 37),List(37,52,2),List(39,0,15)),
        fertilizerToWater = List(List(49,53,8),List(0,11,42),List(42,0,7),List(57,7,4)),
        waterToLight = List(List(88,18,7),List(18,25,70)),
        lightToTemperature = List(List(45,77,23), List(81,45,19), List(68,64,13)),
        temperatureToHumidity = List(List(0,69,1),List(1,0,69)),
        humidityToLocation = List(List(60,56,37),List(56,93,4)) 
      )
    assertEquals(obtained.seeds, expected.seeds, "seeds")
    assertEquals(obtained.seedsToSoil, expected.seedsToSoil, "seedsToSoil")
    assertEquals(obtained.soilToFertilizer, expected.soilToFertilizer, "soilToFertilizer")
    assertEquals(obtained.fertilizerToWater, expected.fertilizerToWater, "fertilizerToWater")
    assertEquals(obtained.waterToLight, expected.waterToLight, "waterToLight")
    assertEquals(obtained.lightToTemperature, expected.lightToTemperature, "lightToTemperature")
    assertEquals(obtained.temperatureToHumidity, expected.temperatureToHumidity, "temperatureToHumidity")
    assertEquals(obtained.humidityToLocation, expected.humidityToLocation, "humidityToLocation")
  }

  /*
  test("Section Map 1") {
    val expected = List(79l,14l,55l,13l).sorted
    val seedsToSoil = List(List(50l, 98l, 2l),List(52l,50l,48l))
    val obtained = sectionMap(List((81l, 1l), (14l, 2l),(57l, 3l),(13l, 4l)), seedsToSoil).map(_._1)
    assertEquals(obtained, expected)
  }*/

  test("Full Part 1 Test") {
    val almanac = new Almanac(
        seeds = List(79,14,55,13), 
        seedsToSoil = List(List(50, 98, 2),List(52,50,48)), 
        soilToFertilizer = List(List(0, 15, 37),List(37,52,2),List(39,0,15)),
        fertilizerToWater = List(List(49,53,8),List(0,11,42),List(42,0,7),List(57,7,4)),
        waterToLight = List(List(88,18,7),List(18,25,70)),
        lightToTemperature = List(List(45,77,23), List(81,45,19), List(68,64,13)),
        temperatureToHumidity = List(List(0,69,1),List(1,0,69)),
        humidityToLocation = List(List(60,56,37),List(56,93,4),List(35,50000,1)) 
      )
    val expected = 35l
    val obtained = part1(almanac)
    assertEquals(obtained, expected)
  }
}
