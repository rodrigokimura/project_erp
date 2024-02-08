Feature: item register
  Scenario: item created from material
    Given there are no items
    When a material is created
    Then there will be an item
  Scenario: item created from tool
    Given there are no items
    When a tool is created
    Then there will be an item

