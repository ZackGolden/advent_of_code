// For more information on writing tests, see
// https://scalameta.org/munit/docs/getting-started.html
class MySuite extends munit.FunSuite {
  test("example test that succeeds") {
    val obtained = 42
    val expected = 42
    assertEquals(obtained, expected)
  }

  test("Calibration Test") {
    val testCalibrationList = List(
      "1abc2",
      "pqr3stu8vwx",
      "a1b2c3d4e5f",
      "treb7uchet"
      )
    val expected = 142
    val actual = generateCalibrationValue(testCalibrationList) 
    assertEquals(actual, expected)
  }

  test("Easy Conversion") {
    val expected = "219"
    val actual = wordToNumber("two1nine")
    assertEquals(actual,expected)
  }

  test("Medium Conversion") {
    val expected = "823"
    val actual = wordToNumber("eightwothree")
    assertEquals(actual, expected)
  }
  test("Hard Conversion") {
    
    val expected = "114818518"
    val actual = wordToNumber("1148pdtcl1eight5oneights")
    assertEquals(actual, expected)
  }

  test("Converted List Test") {
    val testConversionsList = List(
      "two1nine",
      "eightwothree",
      "abcone2threexyz",
      "xtwone3four",
      "4nineeightseven2",
      "zoneight234",
      "7pqrstsixteen"
    )
    val expected = 281
    val actual = generateCalibrationValue(testConversionsList.map(wordToNumber(_)))
    assertEquals(actual, expected)
  }
}
