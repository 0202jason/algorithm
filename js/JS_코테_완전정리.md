# JavaScript 코테 완전 정리 가이드

## 1. 입출력 (I/O)

### 프로그래머스 (가장 일반적)
```javascript
// 문제에서 함수 형태로 주어짐
function solution(arr) {
  return 0;  // 답 반환
}

// 예: 배열 입력
function solution(nums) {
  // nums는 이미 배열로 들어옴
  return nums.reduce((a, b) => a + b);
}

// 예: 문자열 입력
function solution(s) {
  return s.length;
}
```

### 백준 (readline 필요)
```javascript
// Node.js readline 모듈
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const n = parseInt(input[0]);
  const arr = input[1].split(' ').map(Number);
  console.log(solution(n, arr));
  process.exit();
});
```

### 간단한 입출력
```javascript
// 출력
console.log(123);          // 123
console.log('hello');      // hello
console.log(a, b);         // a b (여러 개)

// 한 줄에 공백으로 출력
console.log(arr.join(' ')); // [1,2,3] → "1 2 3"

// 여러 줄 출력
arr.forEach(x => console.log(x));
```

---

## 2. 기본 자료구조 정의 및 생성

### 배열 (Array)
```javascript
// 생성
const arr = [];                    // 빈 배열
const arr = [1, 2, 3];           // 초기값
const arr = new Array(5);         // 길이 5인 배열 (초기화 안 됨)
const arr = Array(5).fill(0);     // 길이 5, 모두 0으로 초기화

// 2D 배열
const matrix = Array(3).fill(null).map(() => Array(3).fill(0));
// [
//   [0, 0, 0],
//   [0, 0, 0],
//   [0, 0, 0]
// ]

// 범위 생성
const range = Array.from({length: 5}, (_, i) => i);
// [0, 1, 2, 3, 4]

// 접근 및 수정
arr[0];           // 첫 번째 요소
arr[arr.length - 1];  // 마지막 요소
arr[0] = 10;      // 수정
```

### 객체 (Object) = 딕셔너리
```javascript
// 생성
const obj = {};                    // 빈 객체
const obj = {a: 1, b: 2};        // 초기값
const obj = new Object();         // 새 객체

// 접근 및 수정
obj.key;           // 속성 접근 (간단한 키)
obj['key'];        // 속성 접근 (숫자나 특수문자)
obj.key = 10;      // 수정
obj['key'] = 10;   // 수정

// 삭제
delete obj.key;

// 체크
'key' in obj;      // true/false
obj.hasOwnProperty('key');  // true/false
```

### Map (더 안전한 딕셔너리)
```javascript
// 생성
const map = new Map();
const map = new Map([['a', 1], ['b', 2]]);  // 초기값

// 접근 및 수정
map.set('key', 10);    // 추가/수정
map.get('key');        // 조회 (없으면 undefined)
map.has('key');        // 포함 여부 (true/false)
map.delete('key');     // 삭제
map.clear();           // 전체 삭제

// 크기
map.size;              // 요소 개수

// 순회
for (const [key, value] of map) {
  console.log(key, value);
}
for (const key of map.keys()) { }
for (const value of map.values()) { }
for (const [k, v] of map.entries()) { }
```

### Set (중복 제거)
```javascript
// 생성
const set = new Set();
const set = new Set([1, 2, 2, 3]);  // {1, 2, 3}

// 추가 및 삭제
set.add(4);            // 추가
set.delete(1);         // 삭제
set.clear();           // 전체 삭제

// 체크
set.has(1);            // true/false

// 크기
set.size;              // 요소 개수

// 순회
for (const x of set) {
  console.log(x);
}

// 배열로 변환
const arr = Array.from(set);
const arr = [...set];  // 더 간단
```

### 스택 (Stack)
```javascript
// 배열로 구현 (LIFO: Last In First Out)
const stack = [];

// push (상단에 추가)
stack.push(1);         // [1]
stack.push(2);         // [1, 2]

// pop (상단에서 제거)
stack.pop();           // 2 반환, [1]

// peek (상단 확인, 제거 X)
stack[stack.length - 1];  // 1

// 비어있는지 확인
stack.length === 0;
```

### 큐 (Queue)
```javascript
// 배열로 구현 (FIFO: First In First Out)
const queue = [];

// enqueue (뒤에 추가)
queue.push(1);         // [1]
queue.push(2);         // [1, 2]

// dequeue (앞에서 제거) ← shift()는 O(n) 주의!
queue.shift();         // 1 반환, [2]

// peek (앞 확인)
queue[0];              // 2

// 최적화 버전 (인덱스 포인터)
let front = 0;
const optimizedQueue = [];
optimizedQueue.push(1);
optimizedQueue.push(2);
const dequeued = optimizedQueue[front++];  // O(1)
```

### 우선순위 큐 (Priority Queue)
```javascript
// 방법 1: 정렬 (간단하지만 느림, O(n log n))
const pq = [];
pq.push([priority, value]);
pq.sort((a, b) => a[0] - b[0]);  // 우선순위 오름차순
const [p, v] = pq.shift();

// 내림차순 (최대값 먼저)
pq.sort((a, b) => b[0] - a[0]);

// 방법 2: 최소 힙 (빠름, O(log n)) - 필요시만 구현
class MinHeap {
  constructor() { this.heap = []; }
  
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  
  pop() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown(0);
    return min;
  }
  
  bubbleUp(idx) {
    while (idx > 0) {
      const parent = Math.floor((idx - 1) / 2);
      if (this.heap[parent] > this.heap[idx]) {
        [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
        idx = parent;
      } else break;
    }
  }
  
  bubbleDown(idx) {
    while (true) {
      let smallest = idx;
      const left = idx * 2 + 1, right = idx * 2 + 2;
      if (left < this.heap.length && this.heap[left] < this.heap[smallest]) smallest = left;
      if (right < this.heap.length && this.heap[right] < this.heap[smallest]) smallest = right;
      if (smallest !== idx) {
        [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
        idx = smallest;
      } else break;
    }
  }
  
  isEmpty() { return this.heap.length === 0; }
}
```

---

## 3. 배열 메서드 (가장 중요!)

### 조회
```javascript
arr.length              // 길이
arr[0]                  // 인덱스 접근
arr.at(-1)              // 뒤에서 첫 번째 (-1, -2, ...)
arr.includes(2)         // 포함 여부 (true/false)
arr.indexOf(2)          // 위치 (없으면 -1)
arr.lastIndexOf(2)      // 마지막 위치
arr.find(x => x > 2)    // 조건 맞는 첫 요소
arr.findIndex(x => x > 2)  // 조건 맞는 첫 인덱스
```

### 추가/제거
```javascript
// 뒤에 추가/제거
arr.push(4)             // 끝에 추가, 새 길이 반환, 원본 수정 O
arr.pop()               // 끝에서 제거, 제거된 요소 반환, 원본 수정 O

// 앞에 추가/제거 (느림! O(n))
arr.unshift(0)          // 앞에 추가, 새 길이 반환, 원본 수정 O
arr.shift()             // 앞에서 제거, 제거된 요소 반환, 원본 수정 O

// 중간에 추가/제거
arr.splice(2, 1, 99)    // index 2에서 1개 제거 후 99 추가, 원본 수정 O
// arr.splice(start, deleteCount, item1, item2, ...)
```

### 부분 추출 (원본 안 건드림)
```javascript
arr.slice(1, 3)         // index 1부터 3 전까지 추출
arr.slice(1)            // index 1부터 끝까지
arr.slice(-2)           // 뒤에서 2개
arr.slice()             // 전체 복사 (얕은 복사)
```

### 변환
```javascript
arr.map(x => x * 2)     // 각 요소 변환
arr.filter(x => x > 2)  // 조건 맞는 요소만
arr.reduce((sum, x) => sum + x, 0)  // 누적 계산
arr.reverse()           // 역순 (원본 수정 O)
arr.sort()              // 정렬 (원본 수정 O, 문자열 기준!)
arr.sort((a, b) => a - b)  // 숫자 정렬 (오름차순)
arr.sort((a, b) => b - a)  // 내림차순
```

### 확인
```javascript
arr.every(x => x > 0)   // 모두 조건 만족? (true/false)
arr.some(x => x > 2)    // 일부 조건 만족? (true/false)
```

### 결합
```javascript
arr.concat([4, 5])      // 배열 연결, 새 배열 반환
arr.join('-')           // 문자열로 합치기 "1-2-3"
arr.flat()              // 중첩 배열 펴기 [[1, 2], [3]] → [1, 2, 3]
arr.flat(2)             // 2단계까지 펴기
```

### 생성
```javascript
Array.from('hello')     // ['h', 'e', 'l', 'l', 'o']
Array.from({length: 5}, (_, i) => i)  // [0, 1, 2, 3, 4]
Array.isArray([1, 2])   // true
```

---

## 4. 문자열 메서드

### 조회
```javascript
str.length              // 길이
str[0]                  // 첫 글자
str.charAt(0)           // 첫 글자 (같음)
str.charCodeAt(0)       // 문자 코드 ('A' → 65)
str.includes('ab')      // 포함 여부
str.indexOf('ab')       // 위치
str.startsWith('hello') // 시작 확인
str.endsWith('world')   // 끝 확인
```

### 추출
```javascript
str.slice(1, 3)         // index 1부터 3 전까지
str.substring(1, 3)     // slice와 비슷 (음수 안 됨)
str.substr(1, 2)        // index 1부터 2글자
str.charAt(0)           // index 0 글자
```

### 변환
```javascript
str.toUpperCase()       // 대문자
str.toLowerCase()       // 소문자
str.trim()              // 앞뒤 공백 제거
str.trimStart()         // 앞 공백 제거
str.trimEnd()           // 뒤 공백 제거
str.split(' ')          // 공백으로 나누기 (배열)
str.split('')           // 글자 단위로 나누기
str.replace('a', 'b')   // 첫 'a'를 'b'로 (원본 안 건드림)
str.replaceAll('a', 'b')  // 모든 'a'를 'b'로
str.repeat(3)           // 3번 반복
str.padStart(5, '0')    // 5글자가 되도록 앞에 '0' 추가
str.padEnd(5, '0')      // 5글자가 되도록 뒤에 '0' 추가
```

### 확인
```javascript
/abc/.test(str)         // 정규식으로 확인 (true/false)
```

---

## 5. 수학 함수

```javascript
Math.abs(-5)            // 절댓값 → 5
Math.floor(3.7)         // 내림 → 3
Math.ceil(3.2)          // 올림 → 4
Math.round(3.5)         // 반올림 → 4
Math.max(1, 2, 3)       // 최댓값 → 3
Math.min(1, 2, 3)       // 최솟값 → 1
Math.max(...arr)        // 배열의 최댓값 (스프레드)
Math.min(...arr)        // 배열의 최솟값
Math.pow(2, 3)          // 2^3 → 8
Math.sqrt(16)           // 제곱근 → 4
Math.random()           // 0 ≤ x < 1
Math.floor(Math.random() * 10)  // 0~9 랜덤
```

---

## 6. 객체/Map 메서드

### 객체
```javascript
Object.keys(obj)        // ['a', 'b'] (키 배열)
Object.values(obj)      // [1, 2] (값 배열)
Object.entries(obj)     // [['a', 1], ['b', 2]]
Object.assign({}, obj)  // 객체 복사 (얕은 복사)

// 순회
for (const key in obj) {
  console.log(key, obj[key]);
}
for (const [key, value] of Object.entries(obj)) {
  console.log(key, value);
}
```

### Map
```javascript
// 이미 위에서 설명함
map.set(key, value)
map.get(key)
map.has(key)
map.delete(key)
map.size
map.clear()

// 순회
for (const [k, v] of map) { }
```

---

## 7. 정렬 (매우 중요!)

### 숫자 정렬
```javascript
// ❌ 틀림! (문자열처럼 정렬됨)
arr.sort();            // [1, 10, 2, 20] ← 잘못됨

// ✅ 맞음
arr.sort((a, b) => a - b);   // 오름차순 [1, 2, 10, 20]
arr.sort((a, b) => b - a);   // 내림차순 [20, 10, 2, 1]
```

### 2D 배열 정렬
```javascript
// 첫 번째 요소로 정렬
arr.sort((a, b) => a[0] - b[0]);

// 첫 번째가 같으면 두 번째로 정렬
arr.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

// 문자열 기준
arr.sort((a, b) => a[0].localeCompare(b[0]));
```

### 객체 배열 정렬
```javascript
const people = [{name: 'Alice', age: 25}, {name: 'Bob', age: 20}];

// age로 정렬
people.sort((a, b) => a.age - b.age);

// name으로 정렬
people.sort((a, b) => a.name.localeCompare(b.name));
```

---

## 8. 형 변환

```javascript
// 문자 → 숫자
parseInt('123')         // 123 (정수)
parseFloat('3.14')      // 3.14 (소수)
Number('123')           // 123
+'123'                  // 123 (트릭)

// 숫자 → 문자
String(123)             // '123'
(123).toString()        // '123'
123 + ''                // '123' (트릭)

// 불린
Boolean(0)              // false
Boolean(1)              // true
Boolean('')             // false
Boolean('hello')        // true
!!0                     // false (트릭, 더블 NOT)
```

---

## 9. 조건문 및 반복 (간단히)

### if/else
```javascript
if (x > 5) {
  // ...
} else if (x > 0) {
  // ...
} else {
  // ...
}

// 삼항 연산자
const result = x > 5 ? 'big' : 'small';
```

### for 루프
```javascript
// 일반 for
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// for...of (요소 순회)
for (const x of arr) {
  console.log(x);
}

// for...in (인덱스 순회, 객체에도 사용)
for (const idx in arr) {
  console.log(arr[idx]);
}

// forEach
arr.forEach((x, idx) => {
  console.log(x, idx);
});

// while
let i = 0;
while (i < arr.length) {
  console.log(arr[i]);
  i++;
}
```

### switch
```javascript
switch (x) {
  case 1:
    // ...
    break;
  case 2:
    // ...
    break;
  default:
    // ...
}
```

---

## 10. 자주 틀리는 함정

### 1. 배열 정렬 (숫자!)
```javascript
[1, 10, 2].sort();              // ❌ [1, 10, 2]
[1, 10, 2].sort((a, b) => a - b);  // ✅ [1, 2, 10]
```

### 2. 배열 복사
```javascript
const a = [1, 2, 3];
const b = a;         // ❌ 같은 참조
const b = [...a];    // ✅ 새 배열 복사
const b = a.slice(); // ✅ 새 배열 복사
```

### 3. 문자열은 불변
```javascript
let str = 'hello';
str[0] = 'H';        // ❌ 안 됨
str = 'H' + str.slice(1);  // ✅ 재할당 필요
```

### 4. shift/unshift는 느림 O(n)
```javascript
// 배열이 크면 느림
arr.shift();  // 모든 요소 한 칸씩 이동

// 큐는 인덱스 포인터 추천
let front = 0;
const dequeued = arr[front++];
```

### 5. includes vs indexOf
```javascript
arr.includes(2)       // true/false
arr.indexOf(2)        // 위치 또는 -1
// 존재만 확인하면 includes, 위치도 필요하면 indexOf
```

### 6. reduce 초기값 필수
```javascript
[1, 2, 3].reduce((sum, x) => sum + x);      // 6 (초기값 1)
[1, 2, 3].reduce((sum, x) => sum + x, 0);   // 6 (초기값 0, 명시)
[]
.reduce((sum, x) => sum + x);                // Error! (초기값 없음)
[].reduce((sum, x) => sum + x, 0);           // 0 (초기값 명시)
```

### 7. Map vs 객체
```javascript
const obj = {1: 'a', 2: 'b'};
const map = new Map([[1, 'a'], [2, 'b']]);

obj[1];        // 'a'
map.get(1);    // 'a'

// Map이 더 안전 (타입 엄격, 모든 타입 키 가능)
const map = new Map();
map.set(1, 'number');
map.set('1', 'string');
map.size;      // 2 (다른 키)
```

### 8. 비교 연산자
```javascript
'10' > '9'      // false (문자열 비교)
10 > 9          // true (숫자 비교)
10 > '9'        // true (자동 형변환)

// == vs ===
10 == '10'      // true (형변환)
10 === '10'     // false (타입도 확인)
// 항상 === 사용!
```

---

## 11. 빈번한 코테 패턴

### 패턴 1: 누적합
```javascript
const prefix = [0];
for (let i = 0; i < arr.length; i++) {
  prefix.push(prefix[i] + arr[i]);
}
// 구간 합: prefix[r+1] - prefix[l]
```

### 패턴 2: 빈도 세기 (Map)
```javascript
const freq = new Map();
for (const x of arr) {
  freq.set(x, (freq.get(x) || 0) + 1);
}
```

### 패턴 3: 투 포인터
```javascript
let left = 0, right = arr.length - 1;
while (left < right) {
  if (arr[left] + arr[right] === target) return true;
  else if (arr[left] + arr[right] < target) left++;
  else right--;
}
```

### 패턴 4: BFS (큐)
```javascript
const queue = [start];
const visited = new Set([start]);
while (queue.length > 0) {
  const node = queue.shift();
  for (const next of graph[node]) {
    if (!visited.has(next)) {
      visited.add(next);
      queue.push(next);
    }
  }
}
```

### 패턴 5: DFS (재귀)
```javascript
function dfs(node, visited) {
  visited.add(node);
  for (const next of graph[node]) {
    if (!visited.has(next)) {
      dfs(next, visited);
    }
  }
}
```

---

## 요약 체크리스트

- [ ] 배열 정렬은 항상 비교함수 (`(a, b) => a - b`)
- [ ] Map/Set 기본 사용법 숙달
- [ ] push/pop vs shift/unshift 성능 차이 인식
- [ ] 문자열은 불변 (재할당 필요)
- [ ] 깊은 복사 vs 얕은 복사 구분
- [ ] === 항상 사용 (== 금지)
- [ ] reduce 초기값 명시
- [ ] 빈도 세기는 Map으로
- [ ] BFS/DFS 템플릿 외우기

---

## 시험장 가져갈 스니펫 (복붙용)

```javascript
// 배열 정렬
arr.sort((a, b) => a - b);

// Map 빈도
const map = new Map();
for (const x of arr) map.set(x, (map.get(x) || 0) + 1);

// BFS 템플릿
const queue = [start];
const visited = new Set([start]);
while (queue.length > 0) {
  const node = queue.shift();
  // 처리
}

// 누적합
const prefix = [0];
for (let i = 0; i < arr.length; i++) {
  prefix.push(prefix[i] + arr[i]);
}

// 투 포인터
let left = 0, right = arr.length - 1;
while (left < right) {
  // 처리
}
```

화이팅! 🚀
