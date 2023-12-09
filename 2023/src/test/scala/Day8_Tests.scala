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
}