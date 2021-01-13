# Created by taske at 13.01.2021
Feature: Fizz buzz test
  # Enter feature description here

  Scenario: Game with argument 15 returns "FizzBuzz"
    Given I create FizzBuzz class
    When I call method game with argument equal 15
    Then I should get result FizzBuzz

  Scenario: Game with argument 5 returns "Buzz"
    Given I create FizzBuzz class
    When I call method game with argument equal 5
    Then I should get result Buzz

  Scenario: Game with argument 3 returns "Fizz"
    Given I create FizzBuzz class
    When I call method game with argument equal 3
    Then I should get result Fizz

  Scenario: Game with argument 7 returns "Not fizz not buzz not fizzbuzz"
    Given I create FizzBuzz class
    When I call method game with argument equal 7
    Then I should get result Not fizz not buzz not fizzbuzz

  Scenario: Game with argument -7 returns "Not fizz not buzz not fizzbuzz"
    Given I create FizzBuzz class
    When I call method game with argument equal -7
    Then I should get result Not fizz not buzz not fizzbuzz
