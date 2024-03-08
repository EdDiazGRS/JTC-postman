const book ={
    title : 'A Little Life',
    author : 'Hanya Yanagihara',
    year: 2015,
    genre: 'contemporary fiction',

}

const serializedBook = JSON.stringify(book);

console.log(serializedBook)