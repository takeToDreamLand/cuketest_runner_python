const { Given, When, Then, Before, setDefinitionFunctionWrapper} = require('cucumber');
const {Util} = require("leanpro.common");
const fs = require('fs');
//// 你的步骤定义 /////
Before(async function(testCase){
	const isDebug = process.env["TEST_VERSION"] === 'debug';
	if(isDebug) log("执行场景: "+testCase.pickle.name);
})

Given("初始值设为{int}", async function (num) {
	this.sum = num;
});

When("现在再加{int}", async function (num) {
	this.sum += num;
});

Then("结果为{int}", async function (num) {
	if (this.sum != num) {
		throw new Error('预期值为 ' + num +
			' 但是实际结果为 ' + this.sum + '.');
	}
});

function log(text){
	let formatedText = `[${new Date().toLocaleString()}]: ${text}\n`;
	fs.writeFileSync('./log.txt', formatedText, {flag: 'a'});
}

