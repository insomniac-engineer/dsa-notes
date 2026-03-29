pattern: Intervals
<h2><a href="https://leetcode.com/problems/meeting-rooms">252. Meeting Rooms</a></h2><h3>Easy</h3><hr><p>Given an array of meeting time <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, determine if a person could attend all meetings.</p>

<p>Note: Meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> false
<strong>Explanation:</strong> The meetings (0,30) and (5,10) overlap.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> true
<strong>Explanation:</strong> No meetings overlap.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,5],[3,9],[6,8]]
<strong>Output:</strong> false
<strong>Explanation:</strong> The meetings (1,5) and (3,9) overlap.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Alternative Link:</strong> <a href="https://www.hellointerview.com/learn/code/intervals/can-attend-meetings">Hello Interview - Can Attend Meetings</a> (LC needs premium)</p>
