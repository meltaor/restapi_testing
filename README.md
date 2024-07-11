# REST API Testing with Postman

This repository contains a collection of tests for the Cat Facts API, implemented using Postman.

## Overview

The tests in this collection aim to ensure the reliability and correctness of the Cat Facts API by validating various aspects of its functionality and response characteristics.

## Test Cases

The following test cases have been developed to validate different aspects of the Cat Facts API:

### Test 1: Validating All Links and Their HTTP Status Codes

- **Endpoint**: [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/)
- **Description**: Validate that all hyperlinks on the page lead to valid URLs and return a status code of 200.
- **Steps**:
  1. Send a GET request to the Cat Facts API.
  2. Extract all hyperlinks from the response.
  3. Send a GET request to each hyperlink to validate the HTTP status code.
  4. Ensure all hyperlinks return a status code of 200.
- **Expected Result**: All hyperlinks should lead to valid URLs and return a status code of 200.

### Test 2: Verify Content-Type Header

- **Endpoint**: [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/)
- **Description**: Ensure that the API endpoint returns the correct Content-Type header in the response.
- **Steps**:
  1. Send a GET request to the Cat Facts API.
  2. Validate the response status code (should be 200).
  3. Check that the Content-Type header exactly matches `text/html; charset=utf-8`.
- **Expected Result**: The response status code should be 200. The Content-Type header in the response should be `text/html; charset=utf-8`.

### Test 3: Validate the Presence of HTML Elements

- **Endpoint**: [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/)
- **Description**: Ensure that specific HTML elements are present in the API response.
- **Steps**:
  1. Send a GET request to the Cat Facts API.
  2. Validate the presence of expected HTML elements in the response.
- **Expected Result**: The API response should contain all expected HTML elements.

### Test 4: Ensure No Sensitive Information in Cookies

- **Endpoint**: [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/)
- **Description**: Validate that no sensitive information is exposed through cookies in the API response.
- **Steps**:
  1. Send a GET request to the Cat Facts API.
  2. Examine the cookies in the response to ensure no sensitive information is present.
- **Expected Result**: Cookies should not contain any sensitive information.

### Test 5: Validate Static Content and Links

- **Endpoint**: [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/)
- **Description**: Ensure that static content (like images, CSS files) and their associated links are valid and accessible.
- **Steps**:
  1. Send a GET request to the Cat Facts API.
  2. Validate the presence and accessibility of static content links (e.g., images, CSS files).
- **Expected Result**: All static content should be present and accessible without any errors.

## Validation Explanation

The validation methods used in these tests were chosen to ensure thorough testing of the Cat Facts API:

- **Test 1** ensures that all links are functional and lead to valid resources, which is crucial for user experience and SEO.
- **Test 2** checks the Content-Type header to verify that the API response format meets expected standards.
- **Test 3** validates the presence of specific HTML elements to ensure the integrity of the API's structure.
- **Test 4** focuses on security by ensuring that no sensitive information is inadvertently exposed through cookies.
- **Test 5** ensures that all static content and associated links are correctly loaded and accessible, enhancing overall usability.

These tests collectively aim to enhance the reliability, security, performance, and usability of the Cat Facts API, ensuring that it meets user expectations and industry standards.
