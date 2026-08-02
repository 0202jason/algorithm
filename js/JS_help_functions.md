# JavaScript에서 Python help() 같은 기능 사용하기

## 1. 가장 간단한 방법 - console.log() 조합

### 객체의 모든 메서드 출력
```javascript
// 배열의 모든 메서드
const arr = [1, 2, 3];
console.log(Object.getOwnPropertyNames(Array.prototype));

// 출력 예:
// [
//   'constructor',
//   'concat',
//   'copyWithin',
//   'fill',
//   'find',
//   'findIndex',
//   'lastIndexOf',
//   'pop',
//   'push',
//   'reverse',
//   'shift',
//   'unshift',
//   'slice',
//   'sort',
//   'splice',
//   'includes',
//   'indexOf',
//   'join',
//   'keys',
//   'values',
//   'entries',
//   'forEach',
//   'filter',
//   'map',
//   'every',
//   'some',
//   'reduce',
//   'reduceRight',
//   'flat',
//   'flatMap',
//   'find',
//   ... (더 많음)
// ]
```

### 객체의 구조 깔끔하게 보기
```javascript
// console.table() - 표 형태로 표시
const arr = [1, 2, 3];
console.table(arr);  // 깔끔한 표 형태

// console.dir() - 모든 속성과 메서드 트리 형태
console.dir(arr);

// console.log() - 기본
console.log(arr);
```

---

## 2. 메서드별 타입 확인

### 특정 메서드가 함수인지 확인
```javascript
const arr = [1, 2, 3];

// 특정 메서드 확인
typeof arr.push;      // 'function'
typeof arr.length;    // 'number'

// 메서드가 존재하는지 확인
'push' in arr;        // true
'map' in arr;         // true
'nonexistent' in arr; // false
```

---

## 3. 더 유용한 헬퍼 함수들

### 함수 1: 객체의 모든 메서드 출력 (Python help() 스타일)
```javascript
function help(obj) {
  const methods = Object.getOwnPropertyNames(Object.getPrototypeOf(obj));
  const funcs = methods.filter(m => typeof obj[m] === 'function');
  const props = methods.filter(m => typeof obj[m] !== 'function');
  
  console.log('=== 메서드 ===');
  funcs.forEach(f => console.log(`  ${f}()`));
  
  console.log('\n=== 속성 ===');
  props.forEach(p => console.log(`  ${p}`));
}

// 사용 예
help([1, 2, 3]);
// 출력:
// === 메서드 ===
//   concat()
//   fill()
//   find()
//   findIndex()
//   ...
// === 속성 ===
//   length
//   ...
```

### 함수 2: 메서드 목록만 깔끔하게
```javascript
function methods(obj) {
  return Object.getOwnPropertyNames(Object.getPrototypeOf(obj))
    .filter(m => typeof obj[m] === 'function')
    .sort();
}

// 사용 예
console.log(methods([1, 2, 3]));
// ['at', 'concat', 'copyWithin', 'entries', 'every', 'fill', 'filter', ...]

console.log(methods(new Map()));
// ['clear', 'delete', 'entries', 'forEach', 'get', 'has', 'keys', 'set', 'values']

console.log(methods('hello'));
// ['charAt', 'charCodeAt', 'codePointAt', 'concat', 'includes', 'indexOf', ...]
```

### 함수 3: 메서드 개수까지 표시
```javascript
function describe(obj) {
  const proto = Object.getPrototypeOf(obj);
  const all = Object.getOwnPropertyNames(proto);
  const funcs = all.filter(m => typeof obj[m] === 'function');
  const props = all.filter(m => typeof obj[m] !== 'function');
  
  console.log(`타입: ${obj.constructor.name}`);
  console.log(`메서드: ${funcs.length}개`);
  console.log(`속성: ${props.length}개`);
  console.log('\n메서드 목록:');
  funcs.sort().forEach(f => console.log(`  - ${f}()`));
}

// 사용 예
describe([1, 2, 3]);
// 타입: Array
// 메서드: 32개
// 속성: 1개
// 
// 메서드 목록:
//   - at()
//   - concat()
//   - copyWithin()
//   ...
```

---

## 4. 실전 활용 예제

### 배열 메서드 확인
```javascript
const arr = [];
console.log(methods(arr));
// ['at', 'concat', 'copyWithin', 'entries', 'every', 'fill', 
// 'filter', 'find', 'findIndex', 'flat', 'flatMap', 'forEach', 
// 'includes', 'indexOf', 'join', 'keys', 'lastIndexOf', 'map', 
// 'pop', 'push', 'reduce', 'reduceRight', 'reverse', 'shift', 
// 'slice', 'some', 'sort', 'splice', 'toLocaleString', 'toString', 
// 'unshift', 'values']
```

### Map 메서드 확인
```javascript
const map = new Map();
console.log(methods(map));
// ['clear', 'delete', 'entries', 'forEach', 'get', 'has', 'keys', 'set', 'values']
```

### Set 메서드 확인
```javascript
const set = new Set();
console.log(methods(set));
// ['add', 'clear', 'delete', 'entries', 'forEach', 'has', 'keys', 'values']
```

### 문자열 메서드 확인
```javascript
const str = '';
console.log(methods(str));
// ['charAt', 'charCodeAt', 'codePointAt', 'concat', 'endsWith', 
// 'includes', 'indexOf', 'lastIndexOf', 'localeCompare', 'match', 
// 'matchAll', 'padEnd', 'padStart', 'repeat', 'replace', 'replaceAll', 
// 'search', 'slice', 'split', 'startsWith', 'substring', 'substr', 
// 'toLowerCase', 'toLocaleLowerCase', 'toUpperCase', 'toLocaleUpperCase', 
// 'trim', 'trimStart', 'trimEnd', ...]
```

---

## 5. 브라우저 개발자 도구에서 사용

### Chrome DevTools 콘솔에서 직접 확인
```javascript
// 콘솔에 직접 입력
[1, 2, 3].  // 탭 누르면 자동완성 메서드 목록 나옴

// 타입핑 후 메서드 확인
const arr = [1, 2, 3];
arr.        // 여기서 탭 누르면 메서드 모두 표시
```

---

## 6. 완전한 help() 함수 (Python 스타일)

```javascript
function help(obj, search = '') {
  const proto = Object.getPrototypeOf(obj);
  const all = Object.getOwnPropertyNames(proto);
  
  const funcs = all
    .filter(m => typeof obj[m] === 'function')
    .filter(m => !search || m.toLowerCase().includes(search.toLowerCase()));
  
  const props = all
    .filter(m => typeof obj[m] !== 'function')
    .filter(m => !search || m.toLowerCase().includes(search.toLowerCase()));
  
  console.log(`\n=== ${obj.constructor.name} ===\n`);
  
  if (funcs.length > 0) {
    console.log('메서드:');
    funcs.sort().forEach(f => {
      console.log(`  ${f}()`);
    });
  }
  
  if (props.length > 0) {
    console.log('\n속성:');
    props.sort().forEach(p => {
      console.log(`  ${p}: ${typeof obj[p]}`);
    });
  }
  
  if (funcs.length === 0 && props.length === 0) {
    console.log('검색 결과 없음');
  }
}

// 사용 예
help([1, 2, 3]);                  // 모든 메서드/속성
help([1, 2, 3], 'map');           // 'map' 포함한 것만
help(new Map(), 'get');           // Map 중 'get' 포함한 것
```

---

## 7. 한 줄로 빠르게 확인

```javascript
// 배열 메서드만 빠르게
Object.getOwnPropertyNames(Array.prototype).filter(m => typeof [1][m] === 'function').sort()

// 정렬된 상태로
console.table(Object.getOwnPropertyNames(Array.prototype).filter(m => typeof [1][m] === 'function').sort())

// Map 메서드
Object.getOwnPropertyNames(Map.prototype).filter(m => typeof new Map()[m] === 'function').sort()
```

---

## 추천: 코테 중에 쓸 도우미

코테 시간이 부족하면 이 짧은 버전 사용:

```javascript
// 복붙용 (시험장에서)
function methods(obj) {
  return Object.getOwnPropertyNames(Object.getPrototypeOf(obj))
    .filter(m => typeof obj[m] === 'function')
    .sort();
}

// 사용
methods([]);         // 배열 메서드
methods(new Map());  // Map 메서드
methods('');         // 문자열 메서드
```

---

## 요약

| 방법 | 사용 예 | 결과 |
|------|--------|------|
| `console.log(arr)` | `console.log([1,2,3])` | 기본 출력 |
| `console.table(arr)` | `console.table([1,2,3])` | 표 형태 |
| `console.dir(arr)` | `console.dir([1,2,3])` | 트리 형태 |
| `Object.getOwnPropertyNames()` | `Object.getOwnPropertyNames(Array.prototype)` | 모든 속성명 배열 |
| `methods()` 함수 | `methods([])` | 함수만 필터링 |
| `help()` 함수 | `help([])` | Python help() 스타일 |

원하는 방식으로 써도 되는데, **코테 중이면 `methods()` 함수 한 줄이 가장 빠르고 편해!**
