$$(".ipc-metadata-list-summary-item").map (item => [ 
item.querySelector(".ipc-title-link-wrapper").href, 
item.querySelector(".ipc-title_text").textContent,
item.querySelector(".cli-title-metadata-item:nth-child(1)").textContent,
item.querySelector(".cli-title-metadata-item:nth-child(2)").textContent,
item.querySelector(".cli-title-metadata-item:nth-child(3)")?.textContent,
item.querySelector(".ipc-rating-star").textContent
])



Array.from(document.querySelectorAll(".ipc-metadata-list-summary-item"))
  .map(item => [ 
    item.querySelector(".ipc-title-link-wrapper")?.href,
    item.querySelector(".ipc-title_text")?.textContent,
    item.querySelector(".cli-title-metadata-item:nth-child(1)")?.textContent,
    parseFloat(item.querySelector(".ipc-rating-star")?.textContent)
  ])
  .filter(movie => movie[3] >= 6 && movie[3] <= 8)
  .slice(0, 25)
  .map(movie => ({
    id: movie[0]?.match(/tt\d+/)?.[0],
    title: movie[1]?.trim(),
    year: movie[2]?.trim(),
    rating: movie[3]
  }))


Array.from(document.querySelectorAll(".ipc-metadata-list-summary-item"))
  .map(item => [ 
    item.querySelector(".ipc-title-link-wrapper")?.href,
    item.querySelector(".ipc-title-link-wrapper")?.textContent,
    item.querySelector(".sc-d5ea4b9d-7")?.textContent,
    parseFloat(item.querySelector(".ipc-rating-star")?.textContent)
  ])
  .filter(movie => movie[3] >= 6 && movie[3] <= 8)
  .slice(0, 25)
  .map(movie => ({
    id: movie[0]?.match(/tt\d+/)?.[0],
    title: movie[1]?.trim(),
    year: movie[2]?.trim(),
    rating: movie[3]
  }));



[{
    "id": "tt13918776",
    "title": "1. The Night Agent",
    "year": "2023–",
    "rating": "7.5"
},
{
    "id": "tt5040012",
    "title": "2. Nosferatu",
    "year": "2024",
    "rating": "7.4"
},
{
    "id": "tt27444205",
    "title": "3. Paradise",
    "year": "2025–",
    "rating": "7.9"
},
{
    "id": "tt8999762",
    "title": "4. The Brutalist",
    "year": "2024",
    "rating": "8"
},
{
    "id": "tt27657135",
    "title": "5. Saturday Night",
    "year": "2024",
    "rating": "7"
},
{
    "id": "tt17526714",
    "title": "6. The Substance",
    "year": "2024",
    "rating": "7.3"
},
{
    "id": "tt10919420",
    "title": "7. Squid Game",
    "year": "2021–2025",
    "rating": "8"
},
{
    "id": "tt26584495",
    "title": "8. Companion",
    "year": "2025",
    "rating": "7.4"
},
{
    "id": "tt13406094",
    "title": "9. The White Lotus",
    "year": "2021–",
    "rating": "8"
},
{
    "id": "tt9218128",
    "title": "10. Gladiator II",
    "year": "2024",
    "rating": "6.6"
},
{
    "id": "tt30057084",
    "title": "11. Babygirl",
    "year": "2024",
    "rating": "6.1"
},
{
    "id": "tt26748649",
    "title": "12. High Potential",
    "year": "2024–",
    "rating": "7.6"
},
{
    "id": "tt28607951",
    "title": "13. Anora",
    "year": "2024",
    "rating": "7.8"
},
{
    "id": "tt14858658",
    "title": "14. Blink Twice",
    "year": "2024",
    "rating": "6.5"
},
{
    "id": "tt16030542",
    "title": "15. The Recruit",
    "year": "2022–",
    "rating": "7.4"
},
{
    "id": "tt7587890",
    "title": "16. The Rookie",
    "year": "2018–",
    "rating": "8"
},
{
    "id": "tt11563598",
    "title": "17. A Complete Unknown",
    "year": "2024",
    "rating": "7.7"
},
{
    "id": "tt18259086",
    "title": "18. Sonic the Hedgehog 3",
    "year": "2024",
    "rating": "7"
},
{
    "id": "tt20215234",
    "title": "19. Conclave",
    "year": "2024",
    "rating": "7.4"
},
{
    "id": "tt21823606",
    "title": "20. A Real Pain",
    "year": "2024",
    "rating": "7.1"
},
{
    "id": "tt16027074",
    "title": "21. Your Friendly Neighborhood Spider-Man",
    "year": "2025–",
    "rating": "6.4"
},
{
    "id": "tt3288518",
    "title": "22. Younger",
    "year": "2015–2021",
    "rating": "7.8"
},
{
    "id": "tt1262426",
    "title": "23. Wicked",
    "year": "2024",
    "rating": "7.6"
},
{
    "id": "tt31186958",
    "title": "24. Prime Target",
    "year": "2025–",
    "rating": "6.4"
},
{
    "id": "tt8008948",
    "title": "25. Den of Thieves 2: Pantera",
    "year": "2025",
    "rating": "6.4"
}]



  
