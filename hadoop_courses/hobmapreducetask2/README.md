# Задание 1

###Исходные данные

Википедия:

* Путь на кластере: /data/wiki/en_articles, семпл: /data/wiki/en_articles_part
* Формат: текст, в каждой строке: идентификатор статьи <tab> текст статьи

## Задача
“Исследование ошибок”. Сервер настроен достаточно сыро, поэтому в логах часто выкидываются ошибки. Админу сервера нужно найти самый забагованный плагин чтоб понять, стоит ли его вообще оставлять на сервере.
Проанализировать стектрейсы ошибок и вывести кол-во ошибок для каждого Java-класса, который их инициирует. Например, такая ошибка
```
[2017-11-29.16:55:43] [Server thread/ERROR]: Could not load 'plugins/figadmin.jar' in folder 'plugins'
org.bukkit.plugin.InvalidDescriptionException: Invalid plugin.yml
	at org.bukkit.plugin.java.JavaPluginLoader.getPluginDescription(JavaPluginLoader.java:162) ~[spigot-1.8.8.jar:git-Spigot-db6de12-18fbb24]
	at org.bukkit.plugin.SimplePluginManager.loadPlugins(SimplePluginManager.java:133) [spigot-1.8.8.jar:git-Spigot-db6de12-18fbb24]
	at org.bukkit.craftbukkit.v1_8_R3.CraftServer.loadPlugins(CraftServer.java:292) [spigot-1.8.8.jar:git-Spigot-db6de12-18fbb24]
	at net.minecraft.server.v1_8_R3.DedicatedServer.init(DedicatedServer.java:198) [spigot-1.8.8.jar:git-Spigot-db6de12-18fbb24]
	at net.minecraft.server.v1_8_R3.MinecraftServer.run(MinecraftServer.java:525) [spigot-1.8.8.jar:git-Spigot-db6de12-18fbb24]
	at java.lang.Thread.run(Thread.java:745) [?:1.7.0_85]
Caused by: java.util.zip.ZipException: error in opening zip file
	at java.util.zip.ZipFile.open(Native Method) ~[?:1.7.0_85]
	at java.util.zip.ZipFile.<init>(ZipFile.java:215) ~[?:1.7.0_85]
	at java.util.zip.ZipFile.<init>(ZipFile.java:145) ~[?:1.7.0_85]
	at java.util.jar.JarFile.<init>(JarFile.java:154) ~[?:1.7.0_85]
	at java.util.jar.JarFile.<init>(JarFile.java:118) ~[?:1.7.0_85]
	at org.bukkit.plugin.java.JavaPluginLoader.getPluginDescription(JavaPluginLoader.java:150)
```
инициирована классом org.bukkit.plugin.java.JavaPluginLoader.getPluginDescription.

* Есть ошибки, в которых нет Stacktrace’а. Их в данной задаче просто игнорируем.
* Номер строки и название файла с кодом (JavaPluginLoader.java:150) следует отсеять при обработке. 
* Следует понимать, что stacktrace читается снизу вверх, поэтому самым информативным для отладки является самое нижнее значение. 


