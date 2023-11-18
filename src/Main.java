import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.IOException;
import java.sql.*;


public class Main {
    public static void main(String[] args) {
        try {
            // Замените URL на адрес вашей веб-страницы с новостями
            String url = "https://iubip.ru/news";

            // Получение HTML-документа
            Document document = Jsoup.connect(url).get();

            // Выбор блока новостей по соответствующему селектору
            Elements newsItems = document.select(".news__item");

            // Перебор элементов блока новостей
            for (Element newsItem : newsItems) {
                // Получение информации о новости (название, текст, дата и т.д.)
                String title = newsItem.select(".news__item a").text();
                String text = newsItem.select(".news__item-text").text();
                String date = newsItem.select(".news__item-date").text();

                // Вывод информации о новости
                System.out.println("Дата: " + date);
                System.out.println("Название: " + title);
                System.out.println("Текст: " + text);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}