import main.scala.day07._
import scala.util.matching.Regex.Match
import munit.Clue.generate

class Day7_Tests extends munit.FunSuite {
  test("Compare 1") {
    val obtained = compareHands("32T3K", "KTJJT")
    assertEquals(obtained, true)
  }

  test("Compare 2") {
    val obtained = compareHands("KK677", "KTJJT")
    assertEquals(obtained, false)
  }

  test("Compare 3") {
    val obtained = compareHands("T55J5", "QQQJA")
    assertEquals(obtained, true)
  }

  test("Find Hand Type 1") {
    val obtained = findHandType("QQQJA")
    assertEquals(obtained, handTypes.threeOfaKind)
  }

  test("Part 1 Ordering test") {
    val hands = List(
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483)
    )
    val obtained = hands.sortWith(lt=(A,B) => compareHands(A._1, B._1))
    val expected = List(("32T3K",765), ("KTJJT",220), ("KK677",28), ("T55J5",684), ("QQQJA",483))
    assertEquals(obtained, expected)
  }

  test("Full Part 1 Test") {
    val hands = List(
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
    )
    val expected = 6440


    val handRegex = """(?<cards>\w+) (?<bid>\d+)""".r
    val obtained = hands.map(handRegex.findFirstMatchIn(_))
        .map(_ match {
            case None => ("", 0)
            case Some(value) => (value.group("cards"), value.group("bid").toInt)
        })
        .sortWith(lt=(A,B) => compareHands(A._1, B._1))
        .zipWithIndex
        .map(a => (a._2+1)*a._1._2)
        .reduce(_ + _)

    assertEquals(obtained, expected)

  }

  test("Part 2 Ordering test") {
    val hands = List(
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483)
    )
    val obtained = hands.sortWith(lt=(A,B) => compareHandsWithJoker(A._1, B._1))
    val expected = List(("32T3K",765), ("KK677",28), ("T55J5",684), ("QQQJA",483), ("KTJJT",220))
    assertEquals(obtained, expected)
  }

  test("Rank with Jokers 1") {

  }

    test("Full Part 2 Test") {
    val hands = List(
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
    )
    val expected = 5905


    val handRegex = """(?<cards>\w+) (?<bid>\d+)""".r
    val obtained = hands.map(handRegex.findFirstMatchIn(_))
        .map(_ match {
            case None => ("", 0)
            case Some(value) => (value.group("cards"), value.group("bid").toInt)
        })
        .sortWith(lt=(A,B) => compareHandsWithJoker(A._1, B._1))
        .zipWithIndex
        .map(a => (a._2+1)*a._1._2)
        .reduce(_ + _)

    assertEquals(obtained, expected)

  }
}
