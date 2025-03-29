{
  "id": "ace1f1cb-80a6-41c8-8f26-22b0fa703992",
  "version": "2.0",
  "name": "Smoke Test",
  "url": "https://kaiharal.github.io/cse270-teton/",
  "tests": [{
    "id": "af3a597b-2efd-48a6-a88b-6233da0bc19d",
    "name": "Home Page Test",
    "commands": [{
      "id": "ee8ac489-f3ba-48ae-b960-ea70cc1ec196",
      "comment": "",
      "command": "open",
      "target": "https://kaiharal.github.io/cse270-teton/",
      "targets": [],
      "value": ""
    }, {
      "id": "3d7c49a6-0b8f-4b64-a36e-6c9577a31e05",
      "comment": "",
      "command": "setWindowSize",
      "target": "1920 x 1080",
      "targets": [],
      "value": ""
    }, {
      "id": "dbd49363-d6ca-4853-95e8-5104118c44ad",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.spotlight1 > .centered-image",
      "targets": [
        ["css=.spotlight1 > .centered-image", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/p", "xpath:idRelative"],
        ["xpath=//section[5]/div/p", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b59f0ec9-9a46-451f-bf8f-3a1e45c2ef65",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.spotlight2 > h4",
      "targets": [
        ["css=.spotlight2 > h4", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/h4", "xpath:idRelative"],
        ["xpath=//div[2]/h4", "xpath:position"],
        ["xpath=//h4[contains(.,'Teton Post Office')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "79de5556-1c92-4156-9544-650c35df44cb",
      "comment": "",
      "command": "assertElementPresent",
      "target": "linkText=Join Us",
      "targets": [
        ["linkText=Join Us", "linkText"],
        ["css=.a-button:nth-child(2)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us')]", "xpath:link"],
        ["xpath=//section[@id='nopad']/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[2]", "xpath:href"],
        ["xpath=//section/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b78c2f47-a0f1-40de-b9f7-50ed08f05b3e",
      "comment": "",
      "command": "click",
      "target": "linkText=Join Us",
      "targets": [
        ["linkText=Join Us", "linkText"],
        ["css=.a-button:nth-child(2)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us')]", "xpath:link"],
        ["xpath=//section[@id='nopad']/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[2]", "xpath:href"],
        ["xpath=//section/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "cb542547-6368-4b2c-95ed-8096d0a8ad61",
    "name": "Directory Page Test",
    "commands": [{
      "id": "329a67ba-a48f-4894-9a25-d4ab8d60c6d5",
      "comment": "",
      "command": "open",
      "target": "https://kaiharal.github.io/cse270-teton/",
      "targets": [],
      "value": ""
    }, {
      "id": "38dcf783-4206-4d03-89f8-48092057bcbb",
      "comment": "",
      "command": "setWindowSize",
      "target": "1920 x 1080",
      "targets": [],
      "value": ""
    }, {
      "id": "dc2de88c-a162-428e-84c5-8df266ee924b",
      "comment": "",
      "command": "waitForElementPresent",
      "target": "linkText=Directory",
      "targets": [
        ["linkText=Directory", "linkText"],
        ["css=li:nth-child(3) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Directory')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'directory.html')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Directory')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "cddb4e38-80b7-4e82-a66f-d9a2f6dc09a0",
      "comment": "",
      "command": "click",
      "target": "linkText=Directory",
      "targets": [
        ["linkText=Directory", "linkText"],
        ["css=.active:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Directory')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'directory.html')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Directory')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "90038bd4-2df5-4435-bfc7-69c6ba9a4e7f",
      "comment": "",
      "command": "click",
      "target": "id=directory-grid",
      "targets": [
        ["id=directory-grid", "id"],
        ["css=#directory-grid", "css:finder"],
        ["xpath=//button[@id='directory-grid']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"],
        ["xpath=//button[contains(.,'GRID')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "efefd716-4f0a-455b-88e8-aead84294cca",
      "comment": "",
      "command": "verifyText",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": "Teton Turf and Tree"
    }, {
      "id": "fa935339-13ce-4d6c-93c9-b88f5a64bf51",
      "comment": "",
      "command": "click",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "d4648823-c117-4a0c-8cc3-6842890e3488",
      "comment": "",
      "command": "verifyText",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": "Teton Turf and Tree"
    }]
  }, {
    "id": "5b9cfe82-9b82-499e-9a9b-a2f44d07c38f",
    "name": "Join Page Test",
    "commands": [{
      "id": "9432125c-174c-4261-bca8-a3f2e8c70a88",
      "comment": "",
      "command": "open",
      "target": "https://kaiharal.github.io/cse270-teton/",
      "targets": [],
      "value": ""
    }, {
      "id": "833a5512-7f54-4f33-97a7-9aa8b9ee2800",
      "comment": "",
      "command": "setWindowSize",
      "target": "1920 x 1080",
      "targets": [],
      "value": ""
    }, {
      "id": "f0ccd63b-2056-413d-9a98-7f198ecede7b",
      "comment": "",
      "command": "waitForElementPresent",
      "target": "linkText=Join",
      "targets": [
        ["linkText=Join", "linkText"],
        ["css=li:nth-child(2) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Join')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'join.html')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "deed3f7f-2fba-4e86-923a-d7b845d23122",
      "comment": "",
      "command": "click",
      "target": "linkText=Join",
      "targets": [
        ["linkText=Join", "linkText"],
        ["css=li:nth-child(2) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Join')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'join.html')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "3b2cfcbc-afc2-47bb-ab9c-db0eeaf5b990",
      "comment": "",
      "command": "assertElementPresent",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6ab1ef85-bf30-445c-9166-3b8054fd8889",
      "comment": "",
      "command": "type",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "Test_FirstName"
    }, {
      "id": "3bc26253-1dce-4d18-9e41-e6b28c376b23",
      "comment": "",
      "command": "click",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "cd5266a2-6e04-4a2f-b389-067440a182c6",
      "comment": "",
      "command": "type",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "Test_LastName"
    }, {
      "id": "58e6fcd6-ad95-4e53-95f4-b94005a529da",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "618107f1-13bb-4c5e-a177-23939b5f66b3",
      "comment": "",
      "command": "type",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": "Test_BusinessName"
    }, {
      "id": "cc745faf-58b5-4fbd-b987-99694bf38691",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "15bafddf-e595-46c2-a751-77707d0f282e",
      "comment": "",
      "command": "type",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": "Test_Position"
    }, {
      "id": "df3dc5f6-089b-48e6-aec7-1a79323c8a61",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "1376ba85-c3a5-48c9-ae6b-56612399c917",
      "comment": "",
      "command": "assertElementPresent",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "52ab5a20-c0de-4d29-b946-3de6bb7a99c8",
    "name": "Admin Page Test",
    "commands": [{
      "id": "b940f4a4-10ab-4e0c-8624-f49df8c6ce7a",
      "comment": "",
      "command": "open",
      "target": "https://kaiharal.github.io/cse270-teton/",
      "targets": [],
      "value": ""
    }, {
      "id": "ad816f57-ebc3-4473-aa8a-359a3ed75a76",
      "comment": "",
      "command": "setWindowSize",
      "target": "1920 x 1080",
      "targets": [],
      "value": ""
    }, {
      "id": "0a111775-57b7-4a43-905a-613be3dcacc3",
      "comment": "",
      "command": "waitForElementPresent",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=li:nth-child(4) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Admin')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[4]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'admin.html')]", "xpath:href"],
        ["xpath=//li[4]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "e9e71e60-4eeb-4270-a4cb-1fd1edb650e0",
      "comment": "",
      "command": "click",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=li:nth-child(4) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Admin')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[4]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'admin.html')]", "xpath:href"],
        ["xpath=//li[4]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "9c9b3787-7ce5-4801-a79d-d7041db43ebd",
      "comment": "",
      "command": "assertElementPresent",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0cc661e9-668e-4831-b6ec-22f991baadd6",
      "comment": "",
      "command": "type",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "test_incorrect_username"
    }, {
      "id": "779c9708-dca5-406a-b41c-1fc403acd05d",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "289e2b48-25b1-4894-9348-e8012006a186",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "test_incorrect_password"
    }, {
      "id": "c7503f53-69c2-4b78-a286-5db984d06c46",
      "comment": "",
      "command": "click",
      "target": "css=.mysubmit:nth-child(4)",
      "targets": [
        ["css=.mysubmit:nth-child(4)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a4ba0b51-868c-47d8-a5d3-6100c4dd2e64",
      "comment": "",
      "command": "waitForText",
      "target": "css=.errorMessage",
      "targets": [
        ["css=.errorMessage", "css:finder"],
        ["xpath=//div[@id='content']/main/section/form/div/span", "xpath:idRelative"],
        ["xpath=//div/span", "xpath:position"],
        ["xpath=//span[contains(.,'Invalid username and password.')]", "xpath:innerText"]
      ],
      "value": "Invalid username and password."
    }]
  }],
  "suites": [{
    "id": "c983d1e2-5e38-4d31-a87f-1fce494379ee",
    "name": "Smoke Test",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["52ab5a20-c0de-4d29-b946-3de6bb7a99c8", "cb542547-6368-4b2c-95ed-8096d0a8ad61", "af3a597b-2efd-48a6-a88b-6233da0bc19d", "5b9cfe82-9b82-499e-9a9b-a2f44d07c38f"]
  }],
  "urls": ["http://127.0.0.1:5500/", "http://127.0.0.1:5500/teton/1.6/index.html", "https://kaiharal.github.io/cse270-teton/"],
  "plugins": []
}