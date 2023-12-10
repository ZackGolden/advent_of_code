import main.scala.day8._

class Day8_Tests extends munit.FunSuite {
  test("example test that succeeds") {
    val obtained = 42
    val expected = 42
    assertEquals(obtained, expected)
  }

  test("First Full Part 1 solution") {
    val mapText = List(
      "RL",
      "",
      "AAA = (BBB, CCC)",
      "BBB = (DDD, EEE)",
      "CCC = (ZZZ, GGG)",
      "DDD = (DDD, DDD)",
      "EEE = (EEE, EEE)",
      "GGG = (GGG, GGG)",
      "ZZZ = (ZZZ, ZZZ)"
    )

    val directions = mapText.head
    val paths = mapText.tail.tail
    val map = mapToMap(paths)

    val expected = 2
    val obtained = navigate(map, directions, "AAA", 0)
    assertEquals(obtained, expected)   
  }

  test("Second Full Part 1 Solution") {
    val mapText = List(
      "LLR",
      "",
      "AAA = (BBB, BBB)",
      "BBB = (AAA, ZZZ)",
      "ZZZ = (ZZZ, ZZZ)"
    )

    val directions = mapText.head
    val paths = mapText.tail.tail
    val map = mapToMap(paths)

    val expected = 6
    val obtained = navigate(map, directions, "AAA", 0)
    assertEquals(obtained, expected)   
  }

  test("GCD 1") {
    val expected = 3.toLong
    val obtained = gcd(12, 15)
    assertEquals(obtained, expected)
  }

  test("GCD 2") {
    val expected = 12.toLong
    val obtained = gcd(12, 24)
    assertEquals(obtained, expected)
  }

  test("LCM 1") {
    val expected = 24.toLong
    val obtained = lcm(12, 24)
    assertEquals(obtained, expected)
  }

  test("Full Part 2 Solution") {
    val mapText = List(
      "LR",
      "",
      "11A = (11B, XXX)",
      "11B = (XXX, 11Z)",
      "11Z = (11B, XXX)",
      "22A = (22B, XXX)",
      "22B = (22C, 22C)",
      "22C = (22Z, 22Z)",
      "22Z = (22B, 22B)",
      "XXX = (XXX, XXX)"
    )

    val directions = mapText.head
    val paths = mapText.tail.tail
    val map = mapToMap(paths)
    val startRegex = """\w\wA""".r
    val startingPoints = map.toList.map(_._1).filter(startRegex.matches(_))
    val endLocations = startingPoints.map(navigateGhosts(map, directions, _, 0).toLong)
    val expected = 6.toLong
    val obtained = endLocations.reduce(lcm(_,_))
    assertEquals(obtained, expected)
  }

}