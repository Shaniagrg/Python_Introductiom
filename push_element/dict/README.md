<h2> Append a value to Dictionary </h2>
<h3>Using Update()</h3>
<p> Syntax .update({key:value})</p>
<ul> 
    <li>It updates the dictionary in-place, which means no new dictionary is created.</li> If a key already exists, its value is updated otherwise, the key-value pair is added.</i>
    <li>
    <li>It is ideal when adding multiplekey-value pairs at once.</li> 
</ul>

<h3>Using assignment operator<h3>
<p>syntax dict[key] = value</p>
<ul>
    <li>It is the fastest way to append a single key-value pair to a dictionary.</li>
    <li>It updates the dictionary in-place without creating a new one</li>
</ul>

<h3>Using setdefault()<h3>
<p>Syntax .setdefault(key,value)</p>
<ul>
    <li>It is  used to ensure a key exists in the dictionary.</li>
    <li>It checks the key first before adding items</li>
    <li>If key already exists it won't add or change the value</li>
</ul>
