// Select all hidden elements (e.g., elements with the d-none class)
const hiddenElements = document.querySelectorAll('.d-none');

// Initialize a variable to store the sum
let sum = 0;

// Iterate through each hidden element
hiddenElements.forEach(hiddenElement => {
  // Find all <div> elements with the class "foo" inside the hidden element
  const fooElements = hiddenElement.querySelectorAll('div.foo');

  // Add their data-value attributes to the sum
  fooElements.forEach(fooElement => {
    const dataValue = parseFloat(fooElement.getAttribute('data-value'));
    if (!isNaN(dataValue)) {
      sum += dataValue;
    }
  });
});

// Output the sum
console.log('Sum of data-value:', sum);
