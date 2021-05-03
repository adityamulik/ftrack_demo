require('isomorphic-fetch');

let fs = require("fs");

const key = fs.readFileSync("../secret.json");

const apiKey = JSON.parse(key);

const ftrack = require('ftrack-javascript-api');

const session = new ftrack.Session(
  'https://self-aditya.ftrackapp.com',
  'adi.mulik2011@gmail.com',
  apiKey.API_Key
);


const asyncCall = async () => {
  // Calling Promise based session
  await session.initializing.then(function () {
    console.info('API session initialized successfully.');
  });
};

asyncCall();

// Retrieve projects using API
const request = session.query('select name from Project');

request.then(res => {
  const projects = res.data;

  console.log(projects);
});

const processData = async () => {
  return 12;
};

processData().then(data => {
  console.log(data);
})
.catch(err => {
  console.log(err)
})