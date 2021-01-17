## About
This plugin will assist in writing better testcode. It will push you to follow best practices.

## Installation

`pip install pylint-testcode-plugin`

## Usage
You can easily load the plugin with the `--load-plugins` flag like below.

`pylint --load-plugins pylint_testcode <your-module-name>.py`

## Checkers
Below an overview of the checkers that come with this plugin. 


| Name | Message : Type | Description |
| --- | --- | --- |
| AssertionsChecker | missing-assertion (error) | You have a test or testcase that has NO assertion. Make sure every test function has an assertion! |
| AbsoluteUrlChecker | no-absolute-url (warning) | Avoid using absolute url in open browser commands. Use a base-url in your project configuration instead. |