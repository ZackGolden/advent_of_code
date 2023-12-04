import main.scala.day2._
class Day2_Tests extends munit.FunSuite {
  test("example test that succeeds") {
    val obtained = 42
    val expected = 42
    assertEquals(obtained, expected)
  }
  test("Test max Cubes from Row") {
    val game1Result = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    val expected = Map[String, Int](("Game", 1), ("blue", 6), ("red", 4), ("green", 2))
    val obtained = maxCubesFromGame(game = game1Result)
    assertEquals(obtained.get("Game"), expected.get("Game"))
    assertEquals(obtained.get("blue"), expected.get("blue"))
    assertEquals(obtained.get("green"), expected.get("green"))
    assertEquals(obtained.get("red"), expected.get("red"))
  }

  test("Positive, is game possible") {
    val game1Result = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    val actualCubes = Map[String, Int](("red",12), ("green", 13), ("blue",14))
    val obtained = isGamePossible(maxCubesFromGame(game = game1Result), actualCubes)
    assert(obtained)
  }

  test("Negative, is game possible") {
    val game3Result = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    val actualCubes = Map[String, Int](("red",12), ("green", 13), ("blue",14))
    val obtained = isGamePossible(maxCubesFromGame(game = game3Result), actualCubes)
    assert(!obtained)
  }

  test("Full Run") {
        val gameResults = List(
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        )
        val actualCubes = Map[String, Int](
            ("red", 12),
            ("green", 13),
            ("blue", 14)
        )
        val expected = 8
        val obtained = gameResults.map(maxCubesFromGame(_)).filter(isGamePossible(_, actualCubes)).map(_.getOrElse("Game", 0)).reduce(_+_)
        assertEquals(obtained, expected)
  }
}