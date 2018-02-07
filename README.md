# ToElement

## Synopsis

平时经常遇到标准 HTML 标签之外的 Element 需要输入。

例如：`<MyHome></MyHome>`

每次输入很麻烦，虽然有 aText 等软件可以作为辅助，但无法覆盖所有的情况。

## Code Example

```js
import React from "react";
import XyzAbc from "...";

class Home extends React.Component {
	render() {
		return (
			<XyzAbc>需要的Element</XyzAbc>
		);
	}
}

export default Home;
```

#### 1) 选择 ZyzAbc

#### 2) `Tools -> To Element` 或者 binding `to_element` command 之后用快捷键

#### 3) 得到 `<XyzAbc></XyzAbc>`

## License(MIT, Apache, etc.)
