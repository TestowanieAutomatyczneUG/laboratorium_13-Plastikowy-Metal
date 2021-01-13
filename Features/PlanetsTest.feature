# Created by taske at 13.01.2021
@planets_setup
Feature: Planets Test
  # Enter feature description here
  Scenario: Calculate age on Merkury
    When I call method new_age with arguments equal 662256000 and Merkury
    Then I should get recalculated age on that Merkury calc

  Scenario: Calculate age on Ziemia
    When I call method new_age with arguments equal 662256000 and Ziemia
    Then I should get recalculated age on that Ziemia calc

  Scenario: Calculate age on Wenus
    When I call method new_age with arguments equal 662256000 and Wenus
    Then I should get recalculated age on that Wenus calc

  Scenario: Calculate age on Mars
    When I call method new_age with arguments equal 662256000 and Mars
    Then I should get recalculated age on that Mars calc

  Scenario: Calculate age on Jowisz
    When I call method new_age with arguments equal 662256000 and Jowisz
    Then I should get recalculated age on that Jowisz calc

  Scenario: Calculate age on Saturn
    When I call method new_age with arguments equal 662256000 and Saturn
    Then I should get recalculated age on that Saturn calc

  Scenario: Calculate age on Uran
    When I call method new_age with arguments equal 662256000 and Uran
    Then I should get recalculated age on that Uran calc

  Scenario: Calculate age on Neptun
    When I call method new_age with arguments equal 662256000 and Neptun
    Then I should get recalculated age on that Neptun calc
