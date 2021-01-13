# Created by taske at 13.01.2021
  @all_pangrams
Feature: Pangram
  # Enter feature description here
  @pangram1
  Scenario: Earth, False
    # Enter steps here
    Given there is a object Pangram
    When string is "Earth"
    Then function returns "False"

  Scenario: Yś, False
    # Enter steps here
    Given there is a object Pangram
    When string is "Yś"
    Then function returns "False"

  Scenario: Lecymy nie spimy, False
    # Enter steps here
    Given there is a object Pangram
    When string is "Lecymy nie spimy"
    Then function returns "False"

  Scenario: Litwo ojczyzna moja, False
    # Enter steps here
    Given there is a object Pangram
    When string is "Litwo ojczyzna moja"
    Then function returns "False"

  Scenario: Pangram, True
    # Enter steps here
    Given there is a object Pangram
    When string is "Waltz, bad nymph, for quick jigs vex"
    Then function returns "True"
  Scenario: Pangram, True
    # Enter steps here
    Given there is a object Pangram
    When string is "Pack my box with five dozen liquor jugs"
    Then function returns "True"
  Scenario: Pangram, True
    # Enter steps here
    Given there is a object Pangram
    When string is "Jackdaws love my big sphinx of quartz"
    Then function returns "True"
  Scenario: Pangram, True
    # Enter steps here
    Given there is a object Pangram
    When string is "The five boxing wizards jump quickly"
    Then function returns "True"
