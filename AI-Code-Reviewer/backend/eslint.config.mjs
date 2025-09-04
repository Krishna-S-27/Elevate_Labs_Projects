// eslint.config.mjs
import js from "@eslint/js";

export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
    },
    rules: {
      "no-unused-vars": "error",
      "no-console": "warn",
      "eqeqeq": ["error", "always"],
      "semi": ["error", "always"],
      "quotes": ["error", "double"],
      "max-depth": ["warn", 3],
      "complexity": ["warn", 10],
    },
  },
  js.configs.recommended,
];
