const os = require('os');
const util = require('util');

const myPlatform = util.format('%s-%s', os.platform(), os.release());

function greengrassHelloWorldRun() {
    console.log("Hello World Greengrass on Lambda");
    console.log(myPlatform);
}

if (!process.env.IS_LAMBDA){
    //execute only greengrass
    setInterval(greengrassHelloWorldRun, 10000);
}

exports.handler = function handler(event, context) {
    //execute only "cloud" lambda
    greengrassHelloWorldRun();
};
