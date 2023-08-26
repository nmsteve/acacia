const fs = require('fs')
const path = require('path');

const imageUrlBase = 'https://ipfs.io/ipfs/bafybeif4wos2tzkan66mjxlsz5oucklzktnlaftnhke7lzmoc4nhso6e7y/'


// Function to generate a random number within a range
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}



const nftAttributes = [
    {
        "trait_type": "Occurence",
        "value": "Rare"
    },
    {
        "trait_type": "Occurence",
        "value": "common"
    },
    {
        "trait_type": "Occurence",
        "value": "Legendary"
    },
    {
        "trait_type": "Occurence",
        "value": "Epic"
    }
];


// Generate metadata for 20 NFTs
for (let i = 1; i <= 20; i++) {
    const nftName = `Acacia #${i}`;
    const imageUrl = `${imageUrlBase}${i}.jpg`; // Assuming images are named like 1.png, 2.png, ...
    //const nftDescription =
    const nftAttribute = nftAttributes[getRandomNumber(0, nftAttributes.length - 1)];


    const nft = {
        name: nftName,
        image: imageUrl,
        attributes: [nftAttribute],

        // Add more properties as needed
    };

    // Convert NFT metadata to JSON format
    const metadataJSON = JSON.stringify(nft, null, 2);

    // Save metadata to a separate file
    const nftFileName = `${i}.json`;
    const filePath = path.join(`./metadata`, nftFileName);
    fs.writeFileSync(filePath, metadataJSON);



}




console.log('NFT metadata generated and saved to separate files.');

