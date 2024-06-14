async function main() {
  const response = await fetch("https://learnwitheunjae.dev/api/sinabro-js/ecommerce")
  const products = await response.json();
  products.map(product => `
    
  `)
}

main();