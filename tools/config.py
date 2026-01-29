# Default Template for Test Case Generation
TEST_CASE_TEMPLATE = """
As an expert QA Engineer, your task is to generate comprehensive test cases for the following feature.
Feature: {user_input}

Output the results in the following JSON format:
{{
  "summary": "High-level summary of the feature",
  "test_cases": [
    {{
      "id": "TC-001",
      "title": "Title of the test case",
      "preconditions": "Any setup needed",
      "steps": ["Step 1", "Step 2"],
      "expected_result": "What should happen",
      "priority": "High|Medium|Low"
    }}
  ]
}}

Ensure all edge cases and negative scenarios are covered.
"""
